import string


def remove_exclamation_marks(s):
    #your code here
    d = {"!":None} 
    t = str.maketrans(d)
    return s.translate(t)
