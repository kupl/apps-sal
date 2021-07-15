import re


def no_space(x):
    res = re.sub(" ", "", x)
    return res
    
no_space("Hi How Are You")

