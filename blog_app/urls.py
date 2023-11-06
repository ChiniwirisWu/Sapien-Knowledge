from django.urls import path
from django.urls import include
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.indexPageView, name='index'),
    path('create_page/', views.createPage, name='create_page'),
    path('remove/<int:page_id>/', views.removePage, name='remove_page'),
    path('read/<int:page_id>/', views.readPageView, name='read_page'),
    path('edit/<int:page_id>/', views.editPageView, name='edit_page'),
    path('update_page/<int:page_id>', views.updatePage, name='update_page'),
    path('remove_question/<int:page_id>', views.removePageQuestionView, name='remove_question'),
    path('author/', views.authorPageView, name='author_page'),
    path('admin_question/', views.adminPageQuestionView, name='admin_question'),
    path('admin_page/', views.adminPageView, name='admin_page'),
    path('error/', views.errorView, name='error_page'),
]



