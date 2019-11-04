from django.contrib import admin

from .models import Post

from parler.admin import TranslatableAdmin

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title','author','publish')
    list_filter = ('created','publish','author')
    search_fields = ('title','body')