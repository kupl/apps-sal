def array_leaders(numbers):
    r=[]
    s=sum(numbers)
    for x in numbers:
        s-=x
        if x>s:
            r.append(x)
    return r
