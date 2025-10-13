from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def home(request):
    return render(request, 'library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'library/category_list.html', {'categories': categories})


