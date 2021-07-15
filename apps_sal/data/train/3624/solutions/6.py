def distribution_of_candy(c):
    i=0
    while min(c)!=max(c):
        i+=1
        a=[(v+v%2)//2 for v in c]
        c=[x+y for x,y in zip(a,a[-1:]+a)]
    return [i, c[0]]
