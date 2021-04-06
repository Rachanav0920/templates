from django.http import HttpResponse
import os
from django.shortcuts import render

file_path=os.path.abspath(__file__)
pro_dir_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_dir_path)

def index(request):
    return ReturnResponse("Hello world")

def page2(request):
    return HttpResponse("<h1>Hey Buddy</h1>")

def page3(request):
    return HttpResponse("<h2>Hello Macha</h2>")

def page4(request):
    contents="""<h1>Hello PANDA</h1>
                 <h1>Bye Panda tc</h1>"""
    return HttpResponse(contents)         

def rend_demo(request):
    return render(request,"sample.html")            
                            