from rest_framework.serializers import Serializer, ModelSerializer
from .models import Book, Chapter, Genre, Author

class BookSerializer(ModelSerializer):

    class Meta:
        model= Book
        fields = '__all__'