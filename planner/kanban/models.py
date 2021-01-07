from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Board(models.Model):
    class Meta:
        db_table = "boards"
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    title = models.CharField(blank=False, null=False, max_length=250, verbose_name="Title")
    create_time = models.DateTimeField(auto_now=True, blank=False, verbose_name="Time of creation")

    def __str__(self):
        return self.title

class BoardUser(models.Model):
    class Meta:
        db_table = "board_users"
        verbose_name = "Board user"
        verbose_name_plural = "Board users"

    board = models.ForeignKey(Board, blank=False, null=False, verbose_name="Board", on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, null=False, verbose_name="User", on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False, blank=False, null=False, verbose_name="Board owner")
    is_read_only = models.BooleanField(default=False, blank=False, null=False, verbose_name="Board can be modified")

    def __str__(self):
        return self.user.name

class BoardColumn(models.Model):
    class Meta:
        db_table = "board_columns"
        verbose_name = "Board column"
        verbose_name_plural = "Board columns"

    board = models.ForeignKey(Board, blank=False, null=False, verbose_name="Board", on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=250, verbose_name="Title")
    create_time = models.DateTimeField(auto_now=True, blank=False, verbose_name="Time of creation")
    sort_index = models.IntegerField(blank=False, default=99, verbose_name="Sort index")

    def __str__(self):
        return self.title


class BoardCard(models.Model):
    class Meta:
        db_table = "board_cards"
        verbose_name = "Board card"
        verbose_name_plural = "Board cards"

    board = models.ForeignKey(Board, blank=False, null=False, verbose_name="Board", on_delete=models.CASCADE)
    column = models.ForeignKey(BoardColumn, blank=False, null=False, verbose_name="Board column", on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=250, verbose_name="Title")
    description = models.CharField(blank=True, null=True, max_length=5000, verbose_name="Description")
    create_time = models.DateTimeField(auto_now=True, blank=False, verbose_name="Time of creation")
    sort_index = models.IntegerField(blank=False, default=99, verbose_name="Sort index")

    def __str__(self):
        return self.title

class BoardUserExecutor(models.Model):
    class Meta:
        db_table = "board_user_executors"
        verbose_name = "Board user executor"
        verbose_name_plural = "Board user executors"

    user = models.ForeignKey(User, blank=False, null=False, verbose_name="User", on_delete=models.CASCADE)
    card = models.ForeignKey(BoardCard, blank=False, null=False, verbose_name="Card", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class BoardCardComment(models.Model):
    class Meta:
        db_table = "board_card_comments"
        verbose_name = "Board card comment"
        verbose_name_plural = "Board card comments"

    user = models.ForeignKey(User, blank=False, null=False, verbose_name="User", on_delete=models.CASCADE)
    card = models.ForeignKey(BoardCard, blank=False, null=False, verbose_name="User", on_delete=models.CASCADE)
    message = models.CharField(blank=True, null=True, max_length=5000, verbose_name="Message")
    create_time = models.DateTimeField(auto_now=True, blank=False, verbose_name="Time of creation")

    def __str__(self):
        return self.user.name + " " + self.card.title + " " + self.message