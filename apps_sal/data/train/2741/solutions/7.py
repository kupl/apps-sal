def russian_peasant_multiplication(x,y):
    prod=0
    while y:
        if y%2:prod+=x
        x+=x
        y=y//2
    return prod
