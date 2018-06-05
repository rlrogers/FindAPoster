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


def get_poster(color):
    for category, colors in POSTERS_BY_COLOR.items():
        if color in colors: 
            return colors[color]
    raise ValueError("You really messed up. Please pick accordingly.")

print(get_poster('magenta'))

"""
color_primary = ["Red", "Yellow", "Blue"]
color_secondary = ["Green", "Purple", "Orange"]
color_tertiary01 = ["Vermillion", "Amber", "Chartreuse"]
color_tertiary02 = ["Teal", "Violet", "Magenta"]

"""