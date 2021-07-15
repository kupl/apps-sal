def greet(name): 
    c=name.lower()
    l=[]
    for i in c:
        l.append(i)
    l[0]=l[0].upper()
    a="".join(l)
    b="Hello "+a+"!"
    return b
