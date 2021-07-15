def josephus_survivor(n,k):
    lst = [i for i in range(1,n+1)]
    x = k-1
    while len(lst) != 1:
        x = x % len(lst)
        lst.pop(x)
        x += k-1
    return lst[0]
    


