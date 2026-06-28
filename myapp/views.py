# views.py
# 功能：處理使用者請求、資料庫操作、頁面渲染與登入/權限控管。
# 本檔只加入說明註解，不更動任何程式邏輯。

# 匯入 Django 內建的會員註冊表單。
from django.contrib.auth.forms import UserCreationForm
# login 用於註冊成功後自動登入使用者。
from django.contrib.auth import login
# login_required 用於限制只有登入會員才能進入指定功能。
from django.contrib.auth.decorators import login_required


from datetime import date
# render：回傳 HTML 頁面；redirect：重新導向；get_object_or_404：查不到資料時回傳 404。
from django.shortcuts import render, redirect, get_object_or_404
# 匯入本專案的資料表模型。
from myapp.models import Book, ReadingRecord

# Paginator 用於資料分頁顯示。
from django.core.paginator import Paginator
# Q 用於建立多條件搜尋；Sum 可用於加總查詢。
from django.db.models import Q, Sum

# staff_member_required 用於限制只有管理員可以操作。
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# 新增書籍
# create_book：管理員新增書籍。
# GET 顯示表單；POST 接收表單資料並新增 Book。
@staff_member_required
def create_book(request):
    # POST 表示使用者送出表單，需處理新增/修改/刪除資料。
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            summary=request.POST.get("summary"),
            category=request.POST.get("category"),
            reward_points=request.POST.get("reward_points"),
            cover_url=request.POST.get("cover_url"),
        )
        return redirect("book_list")

    return render(request, "create_book.html")


# 編輯書籍
# edit_book：管理員編輯既有書籍資料。
@staff_member_required
def edit_book(request, book_id):
    # 依照網址中的 book_id 找到要編輯的書
    # 如果找不到，會自動回傳 404
    book = get_object_or_404(Book, id=book_id)

    # 如果使用者按下「儲存修改」
    if request.method == "POST":

        # 從表單取得新資料，並更新到 book 物件
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.summary = request.POST.get("summary")
        book.category = request.POST.get("category")
        book.reward_points = request.POST.get("reward_points")
        book.cover_url = request.POST.get("cover_url")

        # 儲存修改到資料庫
        book.save()

        # 修改完成後回到書籍列表
        return redirect("book_list")

    # 如果是 GET，代表只是打開編輯頁面
    # 把 book 傳給 edit_book.html，讓表單可以顯示原本資料
    return render(request, "edit_book.html", locals())


# 刪除書籍
# delete_book：管理員刪除書籍。
# 因 Model 設定 CASCADE，刪除書籍時會一併刪除相關閱讀紀錄。
@staff_member_required
def delete_book(request, book_id):
    # 依照網址中的 book_id 找到要刪除的書
    # 如果找不到，會自動回傳 404
    book = get_object_or_404(Book, id=book_id)

    # 如果使用者按下「確認刪除」
    if request.method == "POST":

        # 刪除這本書
        # 注意：因為 ReadingRecord 的 ForeignKey 是 CASCADE
        # 所以這本書相關的閱讀紀錄也會一起被刪除
        book.delete()

        # 刪除完成後回到書籍列表
        return redirect("book_list")

    # 如果是 GET，代表只是打開確認刪除頁面
    # 把 book 傳給 delete_book.html 顯示確認訊息
    return render(request, "delete_book.html", locals())


# register：會員註冊。
# 註冊成功後會自動登入並導向書籍列表。
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book_list")

    else:
        form = UserCreationForm()

    return render(request, "register.html", locals())


# 顯示所有書籍
# book_list：顯示所有書籍，並依建立時間由新到舊排序。
def book_list(request):
    # 從 myapp_book 資料表取得所有書籍
    # 回傳型態：QuerySet[Book]
    books = Book.objects.all().order_by("-created_at")
    print(books)
    return render(request, "book_list.html", locals())


# 0601基本款搜尋分頁與總筆數
# 顯示所有讀者的閱讀紀錄

# reading_record：管理員查看所有讀者的閱讀紀錄。
# 支援關鍵字搜尋、每頁筆數選擇與分頁。
@staff_member_required
def reading_record(request):
    # 取得搜尋關鍵字
    # 例如：/records/?keyword=Sandy
    keyword = request.GET.get("keyword", "")

    # 取得每頁顯示幾筆
    # 例如：/records/?per_page=10
    # 如果沒有選擇，預設 5 筆
    per_page = request.GET.get("per_page", 5)

    # 先取得所有閱讀紀錄
    records = (
        ReadingRecord.objects
        .select_related("book")
        .all()
    )

    # 如果有輸入關鍵字，就進行搜尋
    # 若有輸入關鍵字，依條件過濾查詢結果。
    if keyword:
        records = records.filter(
            Q(reader_name__icontains=keyword) |
            Q(book__title__icontains=keyword) |
            Q(note__icontains=keyword)
        )

    # 依照建立時間由新到舊排序
    records = records.order_by("-created_at")

    # 閱讀筆數統計
    total_records = records.count()

    # 建立分頁器
    # 建立分頁器，將查詢結果切成每頁固定筆數。
    paginator = Paginator(
        records,
        int(per_page)
    )

    # 取得目前頁碼
    page_number = request.GET.get("page")

    # 取得目前頁面的資料
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "reading_record.html",
        locals()
    )


# 顯示單本書的閱讀表單，以及處理提交的閱讀紀錄
# reading_form：登入會員針對指定書籍填寫閱讀心得。
@login_required
def reading_form(request, book_id):
    # book_id 來自網址，例如 /books/1/reading/
    # 這裡會查詢 id=book_id 的書
    # 回傳型態：Book 物件
    book = get_object_or_404(Book, id=book_id)
    print(book)

    # 如果使用者按下提交表單，會以 POST 方式送出資料
    if request.method == "POST":
        
        # 從 HTML 表單取得讀者名稱
        # 回傳型態：str

        # reader_name = request.POST.get("reader_name")
        reader_name = request.user.username

        # 從 HTML 表單取得閱讀心得
        # 回傳型態：str
        note = request.POST.get("note")

        progress = request.POST.get("progress")
        
        if progress == 100:
            lab = True
        else:
            lab = False

        # 新增一筆閱讀紀錄到 myapp_readingrecord 資料表
        ReadingRecord.objects.create(
            book=book,
            reader_name=reader_name,
            note=note,
            progress=progress,
            is_completed=lab,
            earned_points=book.reward_points,
        )


        # 提交成功後，轉到該讀者的紀錄頁面，例如 /readers/Sandy/records/
        return redirect("reader_records", reader_name=reader_name)

    # 如果是 GET，代表只是打開表單頁面
    # 把 book 傳給 reading_form.html
    return render(request, "reading_form.html", locals())

# 編輯閱讀紀錄

# edit_record：編輯閱讀紀錄。
# 管理員可編輯所有紀錄；一般會員只能編輯自己的紀錄。
@login_required
def edit_record(request, record_id):

    if request.user.is_staff:
        record = get_object_or_404(
            ReadingRecord,
            id=record_id
        )
    else:
        record = get_object_or_404(
            ReadingRecord,
            id=record_id,
            reader_name=request.user.username
        )

    if request.method == "POST":
        record.reader_name = request.POST.get(
            "reader_name",
            record.reader_name
        )

        record.note = request.POST.get("note")
        record.progress = request.POST.get("progress")

        if int(record.progress) >= 100:
            record.is_completed = True
            record.earned_points = record.book.reward_points
        else:
            record.is_completed = False
            record.earned_points = 0

        record.save()

        if request.user.is_staff:
            return redirect("reading_record")
        else:
            return redirect(
                "reader_records",
                reader_name=request.user.username
            )

    return render(request, "edit_record.html", locals())



# 刪除閱讀紀錄
# delete_record：刪除閱讀紀錄。
# 管理員可刪除所有紀錄；一般會員只能刪除自己的紀錄。
@login_required
def delete_record(request, record_id):

    if request.user.is_staff:
        record = get_object_or_404(
            ReadingRecord,
            id=record_id
        )
    else:
        record = get_object_or_404(
            ReadingRecord,
            id=record_id,
            reader_name=request.user.username
        )

    reader_name = record.reader_name

    if request.method == "POST":
        record.delete()

        if request.user.is_staff:
            return redirect("reading_record")
        else:
            return redirect(
                "reader_records",
                reader_name=reader_name
            )

    return render(request, "delete_record.html", locals())



# 0601 基本款搜尋分頁與總筆數
# 顯示某位讀者的所有閱讀紀錄

# reader_records：顯示登入會員自己的閱讀紀錄。
# 若使用者嘗試查看別人的紀錄，會自動導回自己的紀錄頁。
@login_required
def reader_records(request, reader_name):

    if reader_name != request.user.username:
        return redirect("reader_records", reader_name=request.user.username)

    keyword = request.GET.get("keyword", "")
    per_page = request.GET.get("per_page", 5)

    records = (
        ReadingRecord.objects
        .select_related("book")
        .filter(reader_name=request.user.username)
    )

    if keyword:
        records = records.filter(
            Q(book__title__icontains=keyword) |
            Q(note__icontains=keyword)
        )

    records = records.order_by("-created_at")

    total_points = sum(
        record.earned_points
        for record in records
    )

    paginator = Paginator(records, int(per_page))
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "reader_records.html", locals())


# 顯示排行榜
# dashboard：顯示登入會員的閱讀統計資料與最新書籍。
@login_required
def dashboard(request):
    total_books = Book.objects.count()

    my_records = ReadingRecord.objects.filter(
        reader_name=request.user.username
    )

    my_record_count = my_records.count()

    my_total_points = sum(
        record.earned_points
        for record in my_records
    )

    latest_books = Book.objects.all().order_by("-created_at")[:5]

    return render(request, "dashboard.html", locals())




