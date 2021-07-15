import textwrap
def morse_converter(string):
    v = (textwrap.wrap(string, 5))
    dicti = {".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0"}
    
    li = []
    for i in v:
        
        li.append(dicti[i])
    
    return (int(''.join(li)))
