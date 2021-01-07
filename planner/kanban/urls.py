from django.urls import path
from .views import *

urlpatterns = [
    path('board/list', BoardsList.as_view()),
    path('board/create', BoardCreate.as_view()),
    path('board/rud/<int:pk>', BoardRUD.as_view()),

    path('column/list', BoardColumnsList.as_view()),
    path('column/create', BoardColumnCreate.as_view()),
    path('column/rud/<int:pk>', BoardColumnRUD.as_view()),

    path('card/list', BoardCardsList.as_view()),
    path('card/create', BoardCardCreate.as_view()),
    path('card/rud/<int:pk>', BoardCardRUD.as_view()),

    path('board_user/list', BoardUsersList.as_view()),
    path('board_user/create', BoardUserCreate.as_view()),
    path('board_user/rud/<int:pk>', BoardUserRUD.as_view()),

    path('executor/list', BoardUserExecutorsList.as_view()),
    path('executor/create', BoardUserExecutorCreate.as_view()),
    path('executor/rud/<int:pk>', BoardUserExecutorRUD.as_view()),

    path('comment/list', BoardCardCommentsList.as_view()),
    path('comment/create', BoardCardCommentCreate.as_view()),
    path('comment/rud/<int:pk>', BoardCardCommentRUD.as_view()),
]