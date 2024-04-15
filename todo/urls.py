"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from todolist import views

app_name = 'todolist'  # 네임스페이스 설정

urlpatterns = [

    # Todo 리스트를 보여주는 URL 패턴
    path('', views.todo_list, name='todo_list'),
    # 새로운 Todo 아이템을 생성하는 URL 패턴
    path('add/', views.add_task, name='add_task'),
    #할 일 상세 정보 URL 패턴
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    # 기존 Todo 아이템을 수정하는 URL 패턴
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    # 기존 Todo 아이템을 삭제하는 URL 패턴
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    # 관리자 전용
    path('admin/', admin.site.urls),
]

