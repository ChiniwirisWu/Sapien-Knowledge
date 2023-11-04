from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# class IndexView(generic.ListView):
    # template_name = 'index.html'
    # context_object_name = 'pages'

    # def get_queryset(self):
        # return models.Page.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]

def indexView(request):
    model = models.Page
    pages = model.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')[:5]
    lastconection = 0;
    if(len(pages) > 0):
        lastconection = pages[0].pub_date
    else:
        lastconection = timezone.now()
    return render(request, 'index.html', context={'pages':pages, 'last_connection':lastconection})


def createPage(request):
    model = models.Page
    description = request.POST['content'][:20] + "..."
    page = model(title = request.POST['title'], content = request.POST['content'], pub_date = timezone.now(), description=description)
    page.save()
    return HttpResponseRedirect(reverse('blog_app:index'))


def readPage(request, page_id):
    model = models.Page
    page = get_object_or_404(model, pk=page_id)
    return render(request, 'page.html', context={'page': page})

def updatPage(request):
    model = models.Page
    page = get_object_or_404(model, pk=request.POST['page_id'])
    page.content = request.POST['content']
    page.title = request.POST['title']
    page.pub_date = timezone.now()
    page.save()
    return HttpResponseRedirect(reverse('blog_app:index'))


def removePage(request, page_id):
    model = models.Page
    page = get_object_or_404(model, pk=page_id)
    page.delete()
    return HttpResponseRedirect(reverse('blog_app:index'))
