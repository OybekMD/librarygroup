from django.contrib import admin
from .models import AuthorModel, BookCategoryModel, BookModel

# Register your models here.

admin.site.register(AuthorModel)
admin.site.register(BookCategoryModel)
admin.site.register(BookModel)
