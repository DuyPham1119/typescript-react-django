from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import BookSerializer
from .models import Book


# class BookList(APIView):

#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except:
#             raise Http404

#     def get_book(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, many=False)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def get_books(self, request, format=None):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def post_book(self, request, format=None):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 50


class BookViewSet(ViewSet):

    queryset = Book.objects.all()
    # pagination_class = StandardResultsSetPagination
    serializer_class = BookSerializer
    
    def list(self, request):
        queryset = Book.objects.all()

        page = int(request.GET['page'])
        print('aaaaaaaaaaaa')
        print(type(page))

        try:
            page = self.pagination_query(queryset)
        except Exception as e:
            page = []
            data = page
            print(e)
            return Response({
                "status": status.HTTP_200_OK,
                "message": 'No more record.',
                "data" : data
                })

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            return self.get_paginated_response(data)


        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Sitting records.',
            "data" : data
        })
        # serializer = BookSerializer(books, many=True)
        # return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
