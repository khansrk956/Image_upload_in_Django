from django.shortcuts import render
from . models import Image
from . forms import ImageForm
# Create your views here.

def home(request):
    if request.method=="POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'myapp/form.html',{'msg':'submit successfully'})
            
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'myapp/form.html',{'form':form,'img':img})

