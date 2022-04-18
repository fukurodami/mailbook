from django.shortcuts import render
from django.views.generic.base import View

from .models import Book

class BookView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books_list.html", {"books_list": books})