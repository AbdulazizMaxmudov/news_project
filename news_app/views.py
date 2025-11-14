from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import News , Category
from .forms import ContactForm

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html', context = context)



def news_detail(request,id):
    news = get_object_or_404(News , id=id  , status=News.Status.Published )
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context = context)

def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        "categories": categories,
    }
    return render(request, 'news/home.html', context = context)

def contactPageView(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h2> biz bilan boglanganizga kata raxmat </h2>")
    context = {
        form: form
    }

    return render(request, 'news/contact.html' , context = context)

def notFoundPageView(request):
    context = {

    }
    return render(request, 'news/404.html' , context = context)
# Create your views here.
