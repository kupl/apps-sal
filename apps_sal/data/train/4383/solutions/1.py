def inclist(a):
    o = [1 for i in a]
    for i in range(1,len(a)):
        if a[i] >= a[i-1]:
            o[i] += o[i-1]
    return o
   
def artificial_rain(garden):
    inc = inclist(garden)
    dec = inclist(garden[::-1])[::-1]
    return max([x + y for x, y in zip(inc, dec)])-1
