def cat_mouse(x,j):
    if len(set(x)) != 4:
        return "boring without all three"
    dog = x.index("D")
    cat = x.index("C")
    mouse = x.index("m")
    if max(cat,mouse) - min(cat,mouse) <= j:
        if min(cat,mouse) < dog and dog < max(cat,mouse):
            return "Protected!"
        return "Caught!"
    
    return "Escaped!"
    


    




