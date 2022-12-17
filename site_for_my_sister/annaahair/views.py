from django.shortcuts import render, redirect
from .models import Annaahair, Annaahair_review
from .forms import Annaahair_reviewForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Annaahair_reviewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('review')
    form = Annaahair_reviewForm()
    context = {'form': form}
    return render(request, 'annaahair/index.html', context)


def contact(request):
    return render(request, 'annaahair/contact.html')


def catalog(request):
    return render(request, 'annaahair/catalog.html')


def review(request):
    form = Annaahair_review.objects.all()
    context = {'form': form}


    return render(request, 'annaahair/review.html', context)


def my_works(request):
    return render(request, 'annaahair/my_works.html')


def blog(request):
    blog1 = Annaahair.objects.all()
    context = {'blog': blog1}
    return render(request, 'annaahair/blog.html', context)


def online_entry(request):
    return render(request, 'annaahair/online_entry.html')
