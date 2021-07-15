def solve(arr):
    print(arr)
    max_l=sorted(arr,reverse=True)
    min_l=sorted(arr)
    l=[]
    for i,a in enumerate(zip(max_l,min_l)):
        if a[0]!=a[1]:
            l.append(a[0])
            l.append(a[1])
        else:
            l.append(a[0])
            break
    return list(dict.fromkeys(l))
