# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404, request
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render, render_to_response, redirect
from models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.template.context_processors import csrf
from django.contrib import auth
from django.core.paginator import Paginator

'''HttpResponse.set_cookie()'''
# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</html></body>" % view
    return HttpResponse(html)
def template_two(request):
    view = "template_two"
    t = loader.get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)
def template_three(request):
    view = 'template_three'
    return render_to_response('myview.html',{'name': view})
page_id =1
def articles(request, page_number=1):
    all_articles = Article.objects.all()
    page_id = current_page = Paginator(all_articles, 3)
    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})


def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

    #def __str__(self):
     #   return self.comments_form


    #article = get_object_or_404(Article, id=article_id)
    #return render(request, 'article.html', {'article': article})
    #html = "<html><body>This is 1 view</html></body>"
    #return HttpResponse(html)

#    return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})

def addlike(request, article_id):
    #back_url = request.META['HTTP_REFERER']
    try:
        if article_id in request.COOKIES:
            #print str(back_url)
            return redirect(request.META['HTTP_REFERER'])
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(request.META['HTTP_REFERER'])


def addcomment (request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/article/get/%s/' % article_id)