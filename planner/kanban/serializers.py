from rest_framework import serializers
from .models import *

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class BoardCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCard
        fields = "__all__"

class BoardColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardColumn
        fields = "__all__"

class BoardUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUser
        fields = "__all__"

class BoardUserExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardUserExecutor
        fields = "__all__"

class BoardCardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardCardComment
        fields = "__all__"