# urls.py
# 功能：設定網站網址路由，將不同 URL 對應到 views.py 中的處理函式。
# 本檔只加入說明註解，不更動任何程式邏輯。

"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

# urlpatterns：網站所有可進入的網址都集中設定在這裡。
urlpatterns = [
    path('admin/', admin.site.urls),


    # Dashboard：登入後查看個人統計資訊。
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),    

    # 會員登入
    # login：使用 Django 內建 LoginView 處理登入。
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    # 會員登出
    # logout：使用 Django 內建 LogoutView 處理登出，登出後回到書籍列表。
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="book_list"
        ),
        name="logout"
    ),


    # 會員註冊
    # register：會員註冊頁面，對應自訂的 views.register。
    path(
        "register/",
        views.register,
        name="register"
    ),



    # 閱讀清單
    # books：顯示全部書籍。
    path(
        'books/', 
        views.book_list, 
        name="book_list"
        ),


    # 新增書籍
    # books/create：管理員新增書籍。
    path(
        "books/create/", 
        views.create_book, 
        name="create_book"
        ),

    # 編輯書籍
    # books/<book_id>/edit：管理員編輯指定書籍。
    path(
        "books/<int:book_id>/edit/", 
        views.edit_book, 
        name="edit_book"
        ),

    # 刪除書籍
    # books/<book_id>/delete：管理員刪除指定書籍。
    path(
        "books/<int:book_id>/delete/", 
        views.delete_book, 
        name="delete_book"
        ),


    # 填寫閱讀筆記
    # books/<book_id>/reading：登入會員提交指定書籍的閱讀心得。
    path(
        "books/<int:book_id>/reading/", 
        views.reading_form, 
        name="reading_form"
        ),

    # 提交過的閱讀紀錄
    # readers/<reader_name>/records：顯示指定讀者的個人閱讀紀錄。
    path(
        "readers/<str:reader_name>/records/", 
        views.reader_records, 
        name="reader_records"
        ),

    # 編輯單筆閱讀紀錄
    # records/<record_id>/edit：編輯單筆閱讀紀錄。
    path(
        "records/<int:record_id>/edit/", 
        views.edit_record, 
        name="edit_record"
        ),

    # 刪除單筆閱讀紀錄
    # records/<record_id>/delete：刪除單筆閱讀紀錄。
    path(
        "records/<int:record_id>/delete/", 
        views.delete_record, 
        name="delete_record"
        ),

    # 所有讀者提交紀錄
    # records：管理員查看全部讀者的閱讀紀錄。
    path(
        'records/', 
        views.reading_record, 
        name="reading_record"
        ),
]

 