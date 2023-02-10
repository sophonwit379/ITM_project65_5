from django.shortcuts import render
from django.http import StreamingHttpResponse
from slrsite.camera import gen

def Index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Team(request):
    return render(request,'team.html')

def Ai(request):
    return render(request,'ai.html')

def video_stream(request):
    return StreamingHttpResponse(gen(),content_type='multipart/x-mixed-replace; boundary=frame')


