from django.db import models
from datetime import datetime
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('a','Admin'),
        ('s','author'),
        ('t','book')
    )

    USERNAME_FIELD = 'username'
    roles = models.CharField(max_length=1,choices=ROLE_CHOICES)

class AuthorModel(models.Model):
    name = models.CharField(max_length=65, default='')
    fname = models.CharField(max_length=65, default='')
    date_of_birth = models.DateField(default=datetime.now)
    country = models.CharField(max_length=15, default='')
    photo = models.ImageField(upload_to="photo/Author/%Y/%m/%d", blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'author'


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=65, default='')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book_category'


class BookModel(models.Model):
    name = models.CharField(max_length=127, default='')
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.SET_NULL, null=True)
    years = models.DateField(default=datetime.now)
    page = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(default=1)
    photo = models.ImageField(upload_to="photo/Book/%Y/%m/%d", blank=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None,null=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'book'