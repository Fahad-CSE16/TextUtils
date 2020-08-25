# i have created this file #fahad
from itertools import count

from django.http import HttpResponse, request
from django.shortcuts import render

""" def index(request):
    return HttpResponse('''<h1>Hello Fahad</h1> <a href="https://www.facebook.com"> Facebook</a> <br> </br>
     <a href="https://www.instagram.com"> Instagram </a> <br> </br>
     <a href="https://www.youtube.com"> Youtube </a> <br> </br>
     <a href="https://www.Codeforces.com"> Codeforces </a> <br> </br>
     <a href="https://www.gmail.com"> Gmail </a>''') """
"""def index(request):
    return HttpResponse('''
    <a href="http://127.0.0.1:8000/spacermv"> SpaceRemove</a> <br> </br>
    <a href="http://127.0.0.1:8000/rmvpunc"> PunctuationRemove</a> <br> </br>
    <a href="http://127.0.0.1:8000/newlinermv"> NewlineRemove</a> <br> </br>
    <a href="http://127.0.0.1:8000/capitalizedfirst"> Capitalizedfirst</a> <br> </br>
    <a href="http://127.0.0.1:8000/Charcount"> Charcount</a> <br> </br>
    ''')"""


def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def analyze(request):
    #getting text
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    makecapital= request.POST.get('makecapital', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countcharacter = request.POST.get('countcharacter', 'off')

    if (countcharacter == "on"):
        num = len(djtext)
        capital = num
        params = {'purpose': 'Number of character in ur text', 'analyzed_text': capital, 'number_of_character' : num}

    if (makecapital == "on"):
        capital = ""
        for char in djtext:
            capital = capital + char.upper()
        params = {'purpose': 'Capital', 'analyzed_text': capital, 'number_of_character' : num}
        djtext = capital
        #return render(request, 'analyze.html', params)

    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~'''
        capital= ""
        for char in djtext:
            if char not in punctuations:
                capital = capital + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': capital, 'number_of_character' : num}
        djtext = capital
       # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        capital = ""
        for index, char in enumerate(djtext):
            if ( djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                capital = capital + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': capital,  'number_of_character' : num}
        #return render(request, 'analyze.html', params)
        djtext = capital

    if (newlineremove == "on"):
        capital = ""
        for char in djtext:
            if char !="\n"  and char !="\r":
                capital = capital + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': capital,  'number_of_character' : num}

    if(newlineremove != "on" and extraspaceremover != "on" and removepunc != "on" and makecapital != "on" and countcharacter != "on"):
        return HttpResponse("Please select any of the options")
    return render(request, 'analyze.html', params)








"""def capitalizedfirst(request):
    return HttpResponse("capitalizedfirst")


def newlinermv(request):
    return HttpResponse("New line remove")


def spacermv(request):
    return HttpResponse("Space remove")


def Charcount(request):
    return HttpResponse("Char COUNT")"""
