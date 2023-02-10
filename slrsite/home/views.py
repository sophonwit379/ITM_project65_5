from django.shortcuts import render

def Index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Team(request):
    return render(request,'team.html')

def Ai(request):
    return render(request,'ai.html')
