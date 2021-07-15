# -*- coding: utf-8 -*-

d = {
    'A':'Ä','E':'Ë','I':'Ï','O':'Ö','U':'Ü','Y':'Ÿ',
    'a':'ä','e':'ë','i':'ï','o':'ö','u':'ü','y':'ÿ'
    
    }
    
def heavy_metal_umlauts(boring_text):

    s = ""

    for i in range(len(boring_text)):
    
        if boring_text[i] in list(d.keys()):
        
            s+= d[boring_text[i]]
            
        else:
        
            s+= boring_text[i]

    return s
    

