def gimme(a):
    for x in a:
        if max(a) > x > min(a):
            return a.index(x) 

