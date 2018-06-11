from itertools import zip_longest

from django.shortcuts import render
from django.http import HttpResponse

# from colors.main import get_matching_poster

HOMEPAGE_COLORS = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'vermilion', 'amber', 'chartreuse', 'teal', 'violet', 'magenta', ]


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {
            'colors_grouped': grouper(HOMEPAGE_COLORS, 3)
        })
    # Add validation here
    # make sure color-selected is in request.POST
    if 'color-selected' not in request.POST:
        
        return render(request, 'index.html', {
            'colors_grouped': grouper(HOMEPAGE_COLORS, 3),
            'error': 'color-not-selected'
        })
    
    selection_option = request.POST['selection-option'] # this is either "match" or "complement"
    color_selected = request.POST['color-selected']
    # Starts of Richard's code:
    # he'll generate this list dinamically based on the color selected by the user
    # for now, i'm just mocking a few as an example:
    posters = [
        "https://www.zazzle.com/sugar_coded_pink_abstract_art_poster_print-228589031082563954",
        "https://www.zazzle.com/sunset_behind_seattle_skyline_from_kerry_park_poster-228488875435299973",
        "https://www.zazzle.com/two_pink_flamingos_on_green_lake_k_turnbull_art_poster-228078145972304476",
    ]
    """
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
    """
    return render(request, 'poster-page.html', {
        'color_selected': color_selected,
        'posters': posters
    })
    
def results(request):
    results = get_complementing_poster
    return HttpResponse('poster-page.html', {'posters': results})


def homepage(request):
    return HttpResponse('index')

