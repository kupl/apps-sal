
def convergents_of_e(m):
    old=2
    new=3
    for i in range(3,m+1):
        temp = old
        old = new
        if i % 3 == 0:
            new = old*((i // 3) * 2) + temp
        else:
            new = old*1+ temp

    new=[int(i) for i in str(new)]
    s=sum(new)
    
    return s
