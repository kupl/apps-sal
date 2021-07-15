import re

def owl_pic(text):
    str = re.sub('[^ 8,W,T,Y,U,I,O,A,H,X,V,M]', '', text.upper())
    return str+"''0v0''"+str[::-1]
