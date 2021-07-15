def josephus(items,k):
    i,res=0,[]
    while items:
        i=(i+k-1)%len(items)
        res+=[items.pop(i)]
    return res
