from .models import Page, User
from django.utils import timezone
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect


#VIEWS
def getLastPublication():
    pages = Page.objects.all().order_by('pub_date')
    if(len(pages) > 0):
        return pages[0].pub_date
    return timezone.now()

def indexPageView(request):
    pages = Page.objects.all()
    last_publication = getLastPublication()
    return render(request, 'index.html', context={'pages':pages, 'last_publication': last_publication})

def authorPageView(request):
    return render(request, 'author.html')

def adminPageView(request):
    lastconnection = getLastPublication()
    try:
        user = User.objects.get(username=request.POST['username'])
    except User.DoesNotExist:
        return render(request, 'error.html')
    if(user.password == request.POST['password']):
        return render(request, 'admin_page.html', context={'pages':Page.objects.all().order_by('pub_date'), 'last_connection': lastconnection})
    else:
        return HttpResponseRedirect(reverse('blog_app:admin_question'))

def readPageView(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except Page.DoesNotExist:
        return HttpResponseRedirect(reverse('blog_app:error_page'))
    return render(request, 'page.html', context={'page': page})

def errorView(request):
    return render(request, 'error.html')

#Question view
def removePageQuestionView(request, page_id):
    try:
        page = get_object_or_404(Page, pk=page_id)
    except Page.DoesNotExist:
        return HttpResponseRedirect(reverse('blog_app:error_page'))
    return render(request, 'remove_question.html', context={'page': page})

def adminPageQuestionView(request):
    return render(request, 'admin_question.html')


#CRUD
def createPage(request):
    description = request.POST['content'][:20] + "..."
    page = Page(title = request.POST['title'], content = request.POST['content'], pub_date = timezone.now(), description=description)
    page.save()
    return HttpResponseRedirect(reverse('blog_app:admin_page'))


def updatePage(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except Page.DoesNotExist:
        return HttpResponseRedirect(reverse('blog_app:error_page'))
    page.title = request.POST['title']
    page.content = request.POST['content']
    page.pub_date = timezone.now()
    page.save()
    return HttpResponseRedirect(reverse('blog_app:read_page'), args=(page_id,))

def removePage(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except Page.DoesNotExist:
        return HttpResponseRedirect(reverse('blog_app:error_page'))
    page.remove()
    return render(request, 'blog_app:index')














