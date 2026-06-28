# models.py
# 功能：定義本專案的資料庫資料表結構。
# 本檔只加入說明註解，不更動任何程式邏輯。

from django.db import models

# Create your models here.

# 資料庫.資料表
# book_sql.myapp_book

# Book：書籍資料表，儲存推薦書籍的基本資訊與閱讀獎勵點數。
class Book(models.Model):
    # 書名：限制最多 100 字。
    title = models.CharField(max_length=100, verbose_name="書名")
    # 作者：限制最多 100 字。
    author = models.CharField(max_length=100, verbose_name="作者")
    # 內容摘要：用 TextField 存放較長文字。
    summary = models.TextField(verbose_name="內容摘要")
    # 分類：例如文學、商管、程式設計等。
    category = models.CharField(max_length=50, verbose_name="分類")
    # 完成閱讀後可獲得的點數。
    reward_points = models.IntegerField(default=0, verbose_name="獎勵點數")
    # 書籍封面圖片網址，可為空值。
    cover_url = models.URLField(blank=True, null=True, verbose_name="封面圖片網址")
    # 建立時間：新增資料時自動記錄。
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    # 在後台或除錯時顯示書名，方便辨識資料。
    def __str__(self):
        return self.title


# book_sql.myapp_readingrecord

# ReadingRecord：閱讀紀錄資料表，記錄使用者針對書籍提交的心得與點數。
class ReadingRecord(models.Model):
    # 對應書籍：一筆閱讀紀錄屬於一本書；書籍刪除時，相關紀錄也會被刪除。
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reading_records",
        verbose_name="對應書籍"
    )
    # 讀者名稱：目前以登入帳號 username 儲存。
    reader_name = models.CharField(max_length=100, verbose_name="讀者名稱")
    # 閱讀心得：允許空值，實際表單端有字數限制。
    note = models.TextField(blank=True, null=True, verbose_name="閱讀心得")
    # 閱讀進度：以 0~100 表示完成比例。
    progress = models.IntegerField(default=0, verbose_name="閱讀進度")
    # 是否完成：用來判斷是否可獲得點數。
    is_completed = models.BooleanField(default=False, verbose_name="是否完成")
    # 已獲得點數：完成閱讀時帶入書籍設定的 reward_points。
    earned_points = models.IntegerField(default=0, verbose_name="已獲得點數")
    # 建立時間：新增資料時自動記錄。
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    # 顯示「讀者 - 書名」，方便辨識閱讀紀錄。
    def __str__(self):
        return f"{self.reader_name} - {self.book.title}"
    
