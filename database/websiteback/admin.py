from django.contrib import admin

from .models import Project, Comment, Message

admin.site.register(Project)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('founder', 'date', 'project', 'text')
    list_filter = ('founder', 'date')
    search_fields = ('founder', 'text', 'project')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'date', 'receiver', 'text', 'title')
    list_filter = ('sender', 'date')
    search_fields = ('sender', 'text', 'date', 'title')
