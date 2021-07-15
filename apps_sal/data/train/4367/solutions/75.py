def area_or_perimeter(l , w):
    l = int(l)   #need to specify it as a integer otherwise it concatanets it and treats it as a string
    w = int(w)
    
    if l == w:
        return l*w 
    else:
        return l+l+w+w
