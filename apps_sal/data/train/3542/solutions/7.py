import math
def owned_cat_and_dog(c, d):
    return [0 if c<15 else 1 if 15<=c<24 else 2 if c==24 else math.floor((c-24)/4+2),0 if d<15 else 1 if 15<=d<24 else 2 if d==24 else math.floor((d-24)/5+2)]

