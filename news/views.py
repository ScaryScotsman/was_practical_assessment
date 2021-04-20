# from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')
    # template = loader.get_template('news/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'news/index.html', context)
