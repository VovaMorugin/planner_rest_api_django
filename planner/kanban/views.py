from django.shortcuts import render
from rest_framework import generics
from .models import Board
# Create your views here.

class BordList(generics.ListAPIView):
    queryset = Board.objects.all()

