from django.db import models
from user.models import CustomUser


STATUS = [
    ('ONGOING', 'ongoing'),
    ('COMPLETED', 'completed'),
]

class Author(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    author_name = models.CharField(max_length=50, null=True, blank=True)
    birth = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.author_name

class Genre(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=False)
    latest_chapter = models.IntegerField(default=0, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    status = models.CharField(max_length=250, choices=STATUS, default='ONGOING')
    url = models.CharField(max_length=250, null=True, blank=False)
    total_view = models.IntegerField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_date']

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    view = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} chapter {self.number}'
