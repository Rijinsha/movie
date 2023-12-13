from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import movie
from .forms import movie_form


# Create your views here.
def index(request):
    #displya datas in front /templates
    mve=movie.objects.all()
    context={                           # its optional
           'movie_list':mve
             }
    return render(request,'index.html',context)
# here movie id is any name
def details(request,movie_id):
    # print all datas in one id to fech
    mv=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mm':mv})


#fech values


  #  return HttpResponse("This is movie number %s" % movie_id) # if any msg print in front page use http

  #-----add movie fun------
def add_movie(request):
    # fetch data
    if request.method=="POST":
        name1=request.POST.get('name')
        desc1 = request.POST.get('desc')
        year1= request.POST.get('year')
        img1= request.FILES ['img']
        #these data add in DB
        movie1=movie(name=name1,desc=desc1,year=year1,img=img1)
        movie1.save()

    return render(request,"add.html")

# --- update data----
def update(request, id):
    movie2=movie.objects.get(id=id)
    form1=movie_form(request.POST or None,request.FILES,instance=movie2)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form1,'movie':movie2})

#-----delete data-----

def delete(request,id):
    if request.method=='POST':
        mv1=movie.objects.get(id=id)
        mv1.delete()
        return redirect('/')
    return render(request,'delete.html')










