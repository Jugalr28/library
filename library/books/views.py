from django.shortcuts import render
from books.models import book
from django.contrib.auth.decorators import login_required
from django.db.models import Q
def home(request):

    return render(request,'home.html')
@login_required
def add_books(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        l=request.POST['l']
        pa=request.POST['pa']
        c=request.FILES['i']
        f=request.FILES.get('f')

        b=book.objects.create(title=t,author=a,price=p,language=l,page=pa,cover=c,pdf=f)
        b.save()
        return view_books(request)
    return render(request,'add.html')
@login_required
def view_books(request):
    k=book.objects.all()
    return render(request,'views.html',{'book':k})
@login_required
def details(request,i):
    k=book.objects.get(id=i)
    return render(request,"details.html",{'book':k})
@login_required
def edit(request,p):

    k = book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['p']
        k.language=request.POST['l']
        k.page=request.POST['pa']
        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.cover=request.FILES['i']
            k.save()
        if(request.FILES.get('f')==None):
            k.save()
        else:
            k.pdf=request.FILES['f']
            k.save()
        return view_books(request)
    return render(request,"edit.html",{'book':k})

@login_required
def delete(request,p):
    k=book.objects.get(id=p)
    k.delete()

    return view_books(request)
def search(request):
    k=None
    if(request.method=="POST"):
        query=request.POST['q']
        print(query)
        if query:
            k=book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

            print(k)


    return render(request,'search.html',{'book':k})
