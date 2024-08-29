from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = ImageForm()  # Reinitialize the form after saving
    else:
        form = ImageForm()  # Initialize a blank form for GET requests

    img = Image.objects.all()  # Fetch images regardless of the request method

    return render(request, 'home.html', {'img': img, 'form': form})
