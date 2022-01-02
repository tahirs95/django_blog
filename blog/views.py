from django.shortcuts import redirect, render
from django.template.defaultfilters import title
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

from .models import Article, Tag
from .forms import ArticleForm
 
def display_view(request):
    context ={}

    if request.method == "POST":
        id = request.POST.get('id')
        tag = get_object_or_404(Tag, id=id)
        context["dataset"] = Article.objects.filter(tags__name__in=[tag])
        context["tags"] = Tag.objects.all()
    else:
        context["dataset"] = Article.objects.all()
        context["tags"] = Tag.objects.all()
    return render(request, "display_view.html", context)

def create_view(request):
    context ={}

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            print('form.cleaned_data.get("tags")')
            print(form.cleaned_data.get("tags"))
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            obj = Article.objects.create(
                                 title = title,
                                 content = content,
                                 image = image
                                 )
            for tag in form.cleaned_data.get("tags"):
                obj.tags.add( tag )
            obj.save()
            print(obj)
            return redirect('display_view')
    else:
        form = ArticleForm()
    context['form']= form
    return render(request, "create_view.html", context)


def detail_view(request, id):
    context ={}
    context["data"] = Article.objects.get(id = id)
         
    return render(request, "detail_view.html", context)
