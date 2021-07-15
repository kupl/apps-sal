def arr(n=0): 
    list = []
    while n != 0:
        list.append(n-1)
        n -= 1
    list.sort()
    return list

