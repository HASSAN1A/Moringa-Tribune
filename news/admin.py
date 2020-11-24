from django.contrib import admin
from .models import Editor,Article,tags,MoringaMerch

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(MoringaMerch)
admin.site.register(tags)
