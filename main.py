#_________________________________________________________________________#
#importing pre-selected photo poster links
#_________________________________________________________________________#
import selection.py *


#_________________________________________________________________________# 
# User selects base color
#Options: Red, Vermilion, Orange, Amber, Yellow, Chartreuse, Green, Teal, Blue, Violet, Purple, Magenta
#_________________________________________________________________________#  
print("Hello, what is your base color? Please choose from Red, Vermilion, Orange, Amber, Yellow, Chartreuse, Green, Teal, Blue, Violet, Purple, or Magenta.")

list = ["red", "vermilion", "orange", "amber", "yellow", "chartreuse", "green", "teal", "blue", "violet", "purple", "magenta"]

color = input()
if color.lower() in list:
    print('Great! For your base color you chose {}'.format(color))
    #continue with rest of program
else:
     print('that color is not in the list, please choose a valid choice!')

#_________________________________________________________________________#
#User input regarding matching or complimenting posters based off of base color
#_________________________________________________________________________# 

print("Now given that you chose {}, please tell us whether you would like to view posters which either match or compliment your base color of {}.".format(color, color))


word = input()
if word.lower() in mc:
    print('Ok, you would like us to {} posters with your color choice of {}.'.format(word, color))
    #continue with rest of program
else:
     print("Are your fingers okay? Please choose either 'match' or 'compliment'")


#_________________________________________________________________________#  
#Functions of match or compliment
#_________________________________________________________________________# 
def base_color():
    choice = 0
    color_primary = ["Red", "Yellow", "Blue"]
    color_secondary = ["Green", "Purple", "Orange"]
    color_tertiary01 = ["Vermillion", "Amber", "Chartreuse"]
    color_tertiary02 = ["Teal", "Violet", "Magenta"]
    return choice
    # User decides if color should match or compliment base
def compliment():
    if choice is color_primary[e]:
        return color_secondary[e]
    if choice is color_secondary[e]:
        return color_primary[e]
    if choice is color_tertiary01[e]:
        return color_tertiary02[e]
    if choice is color color_tertiary02[e]:
        return color_tertiary01[e]
# Recommendations of posters are batched based on match or compliment
def matching():
    if choice is color_primary[e]:
        return color_primary[e]
    if choice is color_secondary[e]:
        return color_secondary[e]
    if choice is color_tertiary01[e]:
        return color_tertiary01[e]
    if choice is color color_tertiary02[e]:
        return color_tertiary02[e]

# Link to posters are presented
