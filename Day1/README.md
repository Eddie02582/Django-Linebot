# Day1

今天建立django專案和把一些基本設定完成


## install package

```
    pip install line-bot-sdk
    pip install django

```

## start django 

首先先建立django 專案
```
    django-admin startproject demoLinebot
```

接著建立Django 應用程式
```
    cd demoLinebot
    python manage.py startapp foodlinebot
```

最後進行資料遷移
```
    python manage.py migrate
```

## 修改setting.py 
INSTALL_APPS 新增 app 
```python
# Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',        
        'foodlinebot',
    ]
```

TEMPLATES 的'DIRS'修改成'DIRS': ['./templates',],
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## 新增對應url
```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foodlinebot/', include('foodlinebot.urls')) 
]
```


