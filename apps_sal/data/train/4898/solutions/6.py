import re
def digit_all (x):
    ## Here you go :
    try:
        return re.sub(r"[\D]",'',x)
    except TypeError:
        return "Invalid input !"
