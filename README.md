# 📚 閱讀管理平台 (Reading Management System)

## 專案介紹

閱讀管理平台是一套使用 Django Framework 開發的 Web 系統，提供會員閱讀書籍、提交閱讀心得、累積閱讀點數以及管理閱讀紀錄等功能。

本系統透過閱讀與點數機制，鼓勵使用者養成閱讀習慣，並提供管理員進行書籍與閱讀紀錄維護。

---

## 系統功能

### 會員功能

* 會員註冊
* 會員登入 / 登出
* 瀏覽書籍列表
* 提交閱讀心得
* 查看個人閱讀紀錄
* 編輯閱讀紀錄
* 刪除閱讀紀錄
* Dashboard 統計資訊

### 管理員功能

* 新增書籍
* 編輯書籍
* 刪除書籍
* 查看所有閱讀紀錄
* 管理閱讀紀錄

---

## 系統架構

```text
使用者
    ↓
URL Routing
    ↓
Views
    ↓
Models
    ↓
MySQL Database
    ↓
Templates
    ↓
畫面呈現
```

本專案採用 Django MTV 架構：

* Model：資料庫模型
* Template：前端頁面
* View：商業邏輯處理

---

## 資料庫設計

### Book

| 欄位            | 說明   |
| ------------- | ---- |
| title         | 書名   |
| author        | 作者   |
| summary       | 內容摘要 |
| category      | 分類   |
| reward_points | 獎勵點數 |
| cover_url     | 封面圖片 |
| created_at    | 建立時間 |

---

### ReadingRecord

| 欄位            | 說明   |
| ------------- | ---- |
| book          | 對應書籍 |
| reader_name   | 讀者名稱 |
| note          | 閱讀心得 |
| progress      | 閱讀進度 |
| is_completed  | 是否完成 |
| earned_points | 獲得點數 |
| created_at    | 建立時間 |

---

## 使用技術

### Backend

* Python 3.x
* Django 6.x

### Frontend

* HTML5
* CSS3
* Django Template

### Database

* MySQL

### Authentication

* Django Authentication

### ORM

* Django ORM

---

## 安裝方式

### 1. Clone Repository

```bash
git clone https://github.com/sandy789456-cyber/01ReadingManagementPlatform.git

cd 專案名稱
```

### 2. 建立虛擬環境

```bash
python -m venv venv
```

啟用虛擬環境

Windows：

```bash
venv\Scripts\activate
```

Mac/Linux：

```bash
source venv/bin/activate
```

### 3. 安裝套件

```bash
pip install -r requirements.txt
```

### 4. 建立 MySQL 資料庫

```sql
CREATE DATABASE book_sql
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

### 5. 設定資料庫連線

修改：

```python
project1/settings.py
```

資料庫設定：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'book_sql',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 6. 執行 Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

### 7. 建立管理員

```bash
python manage.py createsuperuser
```

### 8. 啟動專案

```bash
python manage.py runserver
```

瀏覽器開啟：

```text
http://127.0.0.1:8000
```

---

## 專案畫面

### 書籍列表

* 顯示書籍資訊
* 顯示閱讀獎勵點數
* 提供閱讀單填寫入口

### Dashboard

* 書籍總數
* 我的閱讀紀錄
* 我的總點數

### 閱讀紀錄管理

* 搜尋功能
* 分頁功能
* 編輯功能
* 刪除功能

---

## 未來擴充方向

* 閱讀排行榜
* 點數兌換系統
* Email 通知功能
* 書籍分類篩選
* 圖片上傳功能
* Docker 容器化部署

---

## 開發者

Sandy

閱讀管理平台專案

使用 Django Framework 開發

```
```
