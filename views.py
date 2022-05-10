from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def home(request):
    projects = Article.objects.all()
    return render(request, 'news/home.html', {'projects': projects})


def about(request):
    return render(request, 'news/about.html')


def detail(request, project_id):
    project_detail = get_object_or_404(Article, pk=project_id)
    return render(request, 'news/detail.html', {'article': project_detail})
