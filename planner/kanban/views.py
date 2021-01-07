from rest_framework import generics
from .serializers import *
from rest_framework import generics, filters
import django_filters.rest_framework
from .serializers import *


# Create your views here.


#  Board rest_api classes
class BoardsList(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'title']
    ordering_fields = ['id']

class BoardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BoardCreate(generics.CreateAPIView):
    serializer_class = BoardSerializer


#  BoardColumn rest_api classes
class BoardColumnsList(generics.ListAPIView):
    queryset = BoardColumn.objects.all()
    serializer_class = BoardColumnSerializer

class BoardColumnRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardColumn.objects.all()
    serializer_class = BoardColumnSerializer

class BoardColumnCreate(generics.CreateAPIView):
    serializer_class = BoardColumnSerializer



#BoardCard rest_api classes
class BoardCardsList(generics.ListAPIView):
    queryset = BoardCard.objects.all()
    serializer_class = BoardCardSerializer

class BoardCardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCard.objects.all()
    serializer_class = BoardCardSerializer

class BoardCardCreate(generics.CreateAPIView):
    serializer_class = BoardCardSerializer



#BoardUsers rest_api classes
class BoardUsersList(generics.ListAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer

class BoardUserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUser.objects.all()
    serializer_class = BoardUserSerializer

class BoardUserCreate(generics.CreateAPIView):
    serializer_class = BoardUserSerializer



#BoardUserExecutors rest_api classes
class BoardUserExecutorsList(generics.ListAPIView):
    queryset = BoardUserExecutor.objects.all()
    serializer_class = BoardUserExecutorSerializer

class BoardUserExecutorRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardUserExecutor.objects.all()
    serializer_class = BoardUserExecutorSerializer

class BoardUserExecutorCreate(generics.CreateAPIView):
    serializer_class = BoardUserExecutorSerializer


#BoardCardComments rest_api classes
class BoardCardCommentsList(generics.ListAPIView):
    queryset = BoardCardComment.objects.all()
    serializer_class = BoardCardCommentSerializer

class BoardCardCommentRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardCardComment.objects.all()
    serializer_class = BoardCardCommentSerializer

class BoardCardCommentCreate(generics.CreateAPIView):
    serializer_class = BoardCardCommentSerializer