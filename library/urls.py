from django.urls import path
from . import views

urlpatterns = [
    path('library', views.home, name='library'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('categories/', views.category_list, name='category_list'),
]
