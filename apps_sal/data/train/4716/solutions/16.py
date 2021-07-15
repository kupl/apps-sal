def distribution_of(golds):
    a,b,i=0,0,0
    golds_c=golds[:]
    while golds_c:
        m=golds_c.pop(0) if golds_c[0]>=golds_c[-1] else golds_c.pop()
        if i%2:b+=m
        else:a+=m
        i+=1
    return [a,b]
