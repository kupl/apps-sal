def evil(n):
    n=int(n)
    b =[2**i for i in range(100)]
    d = b[::-1]
    c=0
    for i in d:
        if int(n-i)>=0:
            c+=1
            n-=i
    if c%2==0:
        return "It's Evil!"
    else:
        return "It's Odious!"
    pass
