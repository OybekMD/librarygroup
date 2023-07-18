from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import AuthorModel, BookModel, BookCategoryModel
from .serializers import (AuthorSerializer, BookSerializer, BookCategorySerializer)
from .permissions import IsOwnerPermission

# ------------ Author ------------
# GET, POST
class AllCreateAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerPermission,)

# GET, DELETE
class DetailAuthorView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerPermission,)
    
# UPDATE -> patch, put
class UpdateAuthorView(generics.UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerPermission,)


# ------------ Book Category------------
# GET, POST
class AllCreateBookCategoryView(generics.ListCreateAPIView):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = (IsOwnerPermission,)

# GET, DELETE
class DetailBookCategoryView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = (IsOwnerPermission,)
    
# UPDATE -> patch, put
class UpdateBookCategoryView(generics.UpdateAPIView):
    queryset = BookCategoryModel.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = (IsOwnerPermission,)


# ------------ Book ------------
# GET, POST
class AllCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermission,)

# GET, DELETE
class DetailBookView(generics.RetrieveAPIView, generics.RetrieveDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermission,)
    
# UPDATE -> patch, put
class UpdateBookView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermission,)


