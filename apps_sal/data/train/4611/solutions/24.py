def animals(heads, legs):
    # chick+cow=x
 #   2chick +4cow = y
    # y-2x = 2cow
    # cow = (y-2x)/2
    # chick=x-cow
    chickens = heads - (legs - heads * 2) / 2
    cows = (legs - heads * 2) / 2
    if heads == 0 and legs == 0:
        return (0, 0)
    elif chickens.is_integer() and chickens >= 0 and cows.is_integer and cows >= 0:
        return (chickens, cows)
    else:
        return "No solutions"
