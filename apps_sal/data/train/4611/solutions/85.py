def animals(heads, legs):
    #return (Chickens, Cows)
    cows=legs/2-heads
    chickens=heads-cows
    chick=str(chickens)
    cow=str(cows)
    c1=cow.split('.')
    c2=chick.split('.')
    #print(cows,chickens)
    if c1[1]=='0' and c2[1]=='0':
        if int(chickens)>=0 and int(cows)>=0:
            return (int(chickens),int(cows))
    return 'No solutions'
