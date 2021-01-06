from django.contrib import admin

# Register your models here.

from kanban.models import *

class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time']

class BoardUserAdmin(admin.ModelAdmin):
    list_display = ['board', 'user', 'is_owner', 'is_read_only']

class BoardColumnAdmin(admin.ModelAdmin):
    list_display = ['board', 'title', 'create_time', 'sort_index']

class BoardCardAdmin(admin.ModelAdmin):
    list_display = ['board', 'column', 'title', 'description', 'create_time', 'sort_index']

class BoardUserExecutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'card']

class BoardCardCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'card', 'message', 'create_time']

admin.site.register(Board, BoardAdmin)
admin.site.register(BoardUser, BoardUserAdmin)
admin.site.register(BoardColumn, BoardColumnAdmin)
admin.site.register(BoardCard, BoardCardAdmin)
admin.site.register(BoardUserExecutor, BoardUserExecutorAdmin)
admin.site.register(BoardCardComment, BoardCardCommentAdmin)