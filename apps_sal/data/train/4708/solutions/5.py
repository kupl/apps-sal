def human_years_cat_years_dog_years(h):
    c,d=0,0
    if h == 1:
        c,d=15,15
    elif h>=2:
        c,d=24,24
    for i in range(h-2,0,-1):
        c += 4
        d += 5        
    return [h,c,d]
