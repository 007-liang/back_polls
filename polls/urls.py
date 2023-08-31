from django.urls import path

from . import views

urlpatterns = [
    # 和视图关联上，当访问的时候返回views文件的index
    path("", views.index, name="index"),
]
