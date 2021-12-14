from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import BookForm,CategoryForm

# Create your views here.
def index(request):
    if request.method=='POST':
        data=BookForm(request.POST,request.FILES)
        if data.is_valid():
            data.save()
        add_cat=CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    context={
        'category':Category.objects.all(),
        'books':Books.objects.all(),
        'form':BookForm(),
        'formCat':CategoryForm(),
        'allbooks':Books.objects.filter(active=True).count(),
        'sold':Books.objects.filter(status='sold').count(),
        'rental':Books.objects.filter(status='rental').count(),
        'availble':Books.objects.filter(status='availbe').count(),
        
    }
    return render(request,'pages/index.html',context)

def books(request):
    context={
        'category':Category.objects.all(),
        'books':Books.objects.all()

    }
    return render(request,'pages/books.html',context)
def update(request,id):
    book_id=Books.objects.get(id=id)
    if request.method=='POST':
        data=BookForm(request.POST,request.FILES,instance=book_id)
        if data.is_valid():
            data.save()
        return redirect('/')
    else:
        data=BookForm(instance=book_id)
    context={
        'form':data
    }
 
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_id=get_object_or_404(Books,id=id)
    if request.method=='POST':
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')