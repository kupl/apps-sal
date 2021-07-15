def merged(a,b):
    ac=0
    bc=0
    ra=[]
    while True:
        if ac<len(a) and bc<len(b):
            if a[ac]<b[bc]:
                ra.append(a[ac])
                ac=ac+1
            else:
                ra.append(b[bc])
                bc=bc+1
        elif ac<len(a):
            ra.append(a[ac])
            ac=ac+1
        elif bc<len(b):
            ra.append(b[bc])
            bc=bc+1
        else:
            break
    return ra
def mysort(arr):
    if len(arr)<2:
        return arr
    else:
        mid=len(arr)//2
        part1=mysort(arr[:mid])
        part2=mysort(arr[mid:])
        return merged(part1,part2)
def min_value(digits):
    d={}
    for x in digits:
        d[x]=0
    d=list(d.keys())
    d=mysort(d)
    ans=0
    for x in d:
        ans=(ans*10)+x
    return ans
