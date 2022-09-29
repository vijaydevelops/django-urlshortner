import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Url

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def create(request):
    if request.method == "POST":
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://' + url_details.link)