from django.shortcuts import render
from django.http import StreamingHttpResponse,JsonResponse
from slrsite.camera import gen,getAns


def Index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Team(request):
    return render(request,'team.html')

def Ai(request):
    return render(request,'ai.html')

def Search(request):
    return render(request,'search.html')

def get_data(request):
    data = getAns()
    return JsonResponse({'data':data})

def video_stream(request):
    return StreamingHttpResponse(gen(),content_type='multipart/x-mixed-replace; boundary=frame')


