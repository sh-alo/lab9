
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def list_books(request):
    books = Book.objects.all()  # جلب جميع الكتب من قاعدة البيانات
    return render(request, 'books_app/list_books.html', {'books': books})

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('list_books')
    return render(request, 'books_app/editbook.html', {'book': book})
from django.shortcuts import get_object_or_404

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'books_app/addbook.html', {'form': form})

