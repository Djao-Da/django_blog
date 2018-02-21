from django.contrib import admin

# Register your models here.
from article.models import Article, Comments

class Articleinline(admin.StackedInline):
    model = Comments
    extra = 2

class Articleadmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [Articleinline]
    list_filter = ['article_date']



admin.site.register(Article, Articleadmin)
admin.site.register(Comments)


