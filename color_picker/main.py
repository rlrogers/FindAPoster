#_________________________________________________________________________#
#importing pre-selected photo poster links
#_________________________________________________________________________#
from selection import *
from constant import *
#_________________________________________________________________________# 
# User selects base color
#Options: Red, Vermilion, Orange, Amber, Yellow, Chartreuse, Green, Teal, Blue, Violet, Purple, Magenta
#_________________________________________________________________________#  

#_________________________________________________________________________#  
#Class of match or complement
#_________________________________________________________________________# 
"""The user will pick a base color and choose whether to be presented with posters
    which either match or complement the base color from the selections.py file."""

COMPLEMENT = {
    COLOR_RED: COLOR_GREEN,
    COLOR_YELLOW: COLOR_PURPLE,
    COLOR_BLUE: COLOR_ORANGE,
    COLOR_GREEN: COLOR_RED,
    COLOR_PURPLE: COLOR_YELLOW,
    COLOR_ORANGE: COLOR_BLUE,
    COLOR_VERMILION: COLOR_TEAL,
    COLOR_AMBER: COLOR_VIOLET, 
    COLOR_CHARTREUSE: COLOR_MAGENTA,
    COLOR_TEAL: COLOR_VERMILION,
    COLOR_VIOLET: COLOR_AMBER,
    COLOR_MAGENTA: COLOR_CHARTREUSE
    }


def get_matching_poster(color):
    results = POSTERS_BY_COLOR.get(color)
    if not results: 
	        raise ValueError("You really messed up. Please pick accordingly.")
    return results



def get_complementing_poster(color):
    """Reassign color value to be complement"""  
    color = COMPLEMENT[color]
    results = POSTERS_BY_COLOR.get(color)
    if not results: 
            raise ValueError("You really messed up. Please pick accordingly.")
    return results
    



	    