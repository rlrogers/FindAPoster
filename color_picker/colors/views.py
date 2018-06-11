from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    if request.method == 'GET':
        return render(request, 'index.html')
        
    #Post Request Data
    color = {
        'red':request.POST['red'],
        'yellow':request.POST['yellow'],
        'blue':request.POST['blue'],
        'green':request.POST['green'],
        'purple':request.POST['purple'],
        'orange':request.POST['orange'],
        'vermilion':request.POST['vermilion'],
        'amber':request.POST['amber'],
        'chartreuse':request.POST['chartreuse'],
        'teal':request.POST['teal'],
        'violet':request.POST['violet'],
        'magenta':request.POST['magenta'],
    }
    
    #Dynamic
    color = []
    
    for key, value in request.POST:
        if value == True:
            color.append(key)
        
    return render(request, 'poster-page.html')
    
def homepage(request):
    return HttpResponse('index')

"""Color Posters"""

def red(request):
    # return HttpResponse('Red Posters')
    return render(request, 'red_posters.html')

def yellow(request):
    return HttpResponse('Yellow Posters')
    
def blue(request):
    return HttpResponse('Blue Posters')    

def green(request):
    return HttpResponse('Green Posters')
    
def purple(request):
    return HttpResponse('Purple Posters')
    
def orange(request):
    return HttpResponse('Orange Posters')
    
def vermilion(request):
    return HttpResponse('Vermilion Posters')
    
def amber(request):
    return HttpResponse('Amber Posters')
    
def chartreuse(request):
    return HttpResponse('Chartreuse Posters')
    
def teal(request):
    return HttpResponse('Teal Posters')
    
def violet(request):
    return HttpResponse('Violet Posters')
    
def magenta(request):
    return HttpResponse('Magenta Posters')