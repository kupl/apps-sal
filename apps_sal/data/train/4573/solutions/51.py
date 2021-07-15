def over_the_road(a, n):
    if a%2==0:
        return 1+2*(n-a*0.5)
    else:
        return 2*(n-(a//2))

