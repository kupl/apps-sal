from math import floor,log
def expanded_form(num):
    x = 10**floor(log(num)/log(10))
    a = num//x
    b = num%x
    s = str(a*x) 
    if (b!=0): s += " + " + expanded_form(b)
    return(s)

