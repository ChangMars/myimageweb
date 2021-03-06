from django.shortcuts import render, redirect
from .models import Photo
from .forms import UploadModelForm

# Create your views here.


def index(request):

    photos = Photo.objects.all()

    form = UploadModelForm()

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/app')

    context = {
        'photos': photos,
        'form': form
    }

    return render(request, 'photos/index.html', context)
