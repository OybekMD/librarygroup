from django.urls import path
from .views import AllCreateAuthorView, DetailAuthorView, UpdateAuthorView
from .views import AllCreateBookCategoryView, DetailBookCategoryView, UpdateBookCategoryView
from .views import AllCreateBookView, DetailBookView, UpdateBookView

urlpatterns = [
    path('author', AllCreateAuthorView.as_view()),
    path('author/<int:pk>', DetailAuthorView.as_view()),

    path('bookcategory', AllCreateBookCategoryView.as_view()),
    path('bookcategory/<int:pk>', DetailBookCategoryView.as_view()),

    path('book', AllCreateBookView.as_view()),
    path('book/<int:pk>', DetailBookView.as_view()),
]