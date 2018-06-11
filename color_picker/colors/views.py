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
    
