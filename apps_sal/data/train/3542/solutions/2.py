def owned_cat_and_dog(cat, dog):
    return [years(cat, 4), years(dog, 5)]
    
def years(a, m):
    return 2 + (a - 24)//m if a >= 24 else 1  if a >= 15 else 0

