from itertools import zip_longest

from django.shortcuts import render
from django.http import HttpResponse

from main import get_matching_poster
from selection import *

HOMEPAGE_COLORS = ['red', 'blue', 'yellow', 'green', 'purple', 'orange', 'vermilion', 'amber', 'chartreuse', 'teal', 'violet', 'magenta']


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
    def get_matching_poster(color):
        results = POSTERS_BY_COLOR.get(color)
        if not results: 
	            raise ValueError("You really messed up. Please pick accordingly.")
        return results
    
    # for now, i'm just mocking a few as an example:
    # posters = [
    #     "https://www.zazzle.com/sugar_coded_pink_abstract_art_poster_print-228589031082563954",
    #     "https://www.zazzle.com/sunset_behind_seattle_skyline_from_kerry_park_poster-228488875435299973",
    #     "https://www.zazzle.com/two_pink_flamingos_on_green_lake_k_turnbull_art_poster-228078145972304476",
    # ]
    posters = []
    
    if selection_option == 'match':
        answer = POSTERS_BY_COLOR.get(color_selected)
    
    elif selection_option == 'complement':
        answer = POSTERS_BY_COLOR.get(COMPLEMENT[color_selected])
            
            
    
    return render(request, 'poster-page.html', {
        'color_selected': color_selected,
        'posters': answer
    })
    
def results(request):
    results = get_complementing_poster
    return HttpResponse('poster-page.html', {'posters': results})


def homepage(request):
    return HttpResponse('index')

