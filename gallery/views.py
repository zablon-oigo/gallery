from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Photo
from .forms import AddPhoto
from django.db.models import Q
def home(request):
    categories=Category.objects.all()
    photos=Photo.objects.all()
    return render(request,'gallery/index.html',{'categories':categories,'photos':photos})

def search_photo(request):
    categories=Category.objects.all()
    photos=Photo.objects.all()
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)
    if category_id:
        photos=photos.filter(category_id=category_id)
    if query:
        photos=photos.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request,'gallery/search.html',{
        'query':query,
        category_id:int(category_id),
        'photos':photos,
        'categories':categories,
    })


def photo_detail(request,id):
    photo=get_object_or_404(Photo,id=id)
    related_photo=Photo.objects.filter(category=photo.category).exclude(id=id)[0:3]
    return render(request,'gallery/detail.html',{'photo':photo,'related_photo':related_photo})

def delete_photo(request,id):
    query=Photo.objects.filter(created_by=request.user)
    photo=get_object_or_404(query, id=id)
    if request.method =='POST':
        photo.delete()
        return redirect('home')
    return render(request,'gallery/delete.html',{'photo':photo})

def create_photo(request):
    if request.method =='POST':
        form=AddPhoto(request.POST,request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=request.user
            user.save()
            return redirect('detail', id=user.id)
    else:
            form=AddPhoto()
    return render(request, 'gallery/create.html', {'form':form})
def update_photo(request,id):
    photo=get_object_or_404(Photo, id=id)
    form=AddPhoto(instance=photo)
    if request.method =='POST':
        form=AddPhoto(request.POST,instance=photo)
        if form.is_valid():
            user=form.save(commit=False)
            user.created_by=request.user
            user.save()
            return redirect('detail', id=user.id)
        
    return render(request,'gallery/create.html',{'form':form,'id':id})
 

        
        
            
    
