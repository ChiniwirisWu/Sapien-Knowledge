from django.urls import path
from django.urls import include
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('create_page/', views.createPage, name='create_page'),
    path('remove/<int:page_id>/', views.removePage, name='remove_page'),
    path('read/<int:page_id>/', views.readPage, name='read_page'),
    path('update_page/', views.updatPage, name='update_page'),
]



