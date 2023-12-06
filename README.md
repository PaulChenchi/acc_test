# ACC_TEST 

### 建立虛擬環境
- pip install pipenv
- pipenv shell

### 安裝套件
- pip install django

### 產生專案
- django-admin startproject 專案名稱 .

### 啟動Server
- python manage.py runserver

### 同步資料庫跟建立資料表
- python manage.py makemigrations
- python manage.py migrate

### 建立超級使用者
- python manage.py createsuperuser

### 建立網頁功能
- python manage.py startapp user

### 註冊功能
- settings
    - INSTALL_APP 進行新增





# Todolist

### 建立虛擬環境
- pip install pipenv
- pip shell

### 安裝套件
- pip install django

### 產生專案
- django-admin startproject todolist .
    - . => 本地產生需求的目錄跟檔按

### 啟動Server
- python manage.py runserver


### 同步資料庫跟建立資料表
- python manage.py makemigrations
- python manage.py migrate

### 建立超級使用者
- python manage.py createsuperuser

### 建立網頁功能
- python manage.py startapp acc(功能)

### 註冊功能
- settings   # 註冊apps裡的class
    - INSTALL_APP 進行新增


### views 寫功能


### urls分配網址route

### 繼承網頁templates
