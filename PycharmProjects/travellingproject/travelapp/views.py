import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from travelapp.models import Login, User


def login(request):
    return render(request,'login.html')


def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('Logout');window.location='/'</script>''')



def adminpage(request):
    return render(request,'adminindex.html')

def userpage(request):
    return render(request,'userindex.html')


def add_user(request):
    return render(request,'user.html')


def add_user_POST(request):
    username=request.POST['username']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']

    # fs = FileSystemStorage()
    # date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.JPG'
    # fs.save(date, image)
    # path= fs.url(date)
    #
    #
    a=Login()
    a.username=email
    a.password=password
    a.type="user"
    a.save()



    b=User()
    b.username=username
    b.first_name=first_name
    b.last_name=last_name
    b.email=email
    b.password=password
    b.confirm_password=confirm_password
    b.LOGIN=a
    b.save()

    return HttpResponse('''<script>alert('success');window.location='/'</script>''')






def login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    l=Login.objects.filter(username=username,password=password)

    if l.exists():
        m=Login.objects.get(username=username,password=password)
        request.session['lid']=m.id


        if m.type=='admin':
            return redirect('/adminpage')

        elif m.type=="user":

                return redirect('/userpage')


        else:
            return redirect('/')


    else:
        return redirect('/')










