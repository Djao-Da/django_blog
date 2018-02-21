# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
short_text_len = 50
class Article(models.Model):
    class Meta():
        db_table = "article"

    article_title = models.CharField(max_length= 200)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)
    short_text_len = 50
    def get_short_text(self):
        if len(self.article_text)>short_text_len:
            return self.article_text[:short_text_len]
        else:
            return self.article_text


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
        verbose_name_plural = "Comments"

    comment_date = models.DateField(auto_now=True)
    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_article = models.ForeignKey(Article)

'''    def __str__(self):
        return self.comments_text
'''
