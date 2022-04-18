from datetime import date

from django.db import models


class Author(models.Model):
    """Автор книги"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Publisher(models.Model):
    """Издатель книги"""
    name = models.CharField("Имя", max_length=30)
    address = models.CharField("Адрес", max_length=50)
    city = models.CharField("Город", max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    authors = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publisher, verbose_name="Издательство", on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField("Дата публикации", default=date.today)
    stock = models.PositiveIntegerField("Запас", default=1)
    image = models.ImageField("Изображение", upload_to="books/")
    price = models.PositiveIntegerField("Цена", default=0)
    url = models.SlugField(max_length=160, unique=True)
    description = models.CharField("Аннотация", max_length=300)
    existence = models.BooleanField("Наличие")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"




