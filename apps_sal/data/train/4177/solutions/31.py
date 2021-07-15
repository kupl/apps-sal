def men_from_boys(arr):
    a=[]
    b=[]
    for x in arr:
        if x%2==0:
            if x not in a:
                a.append(x)
            else:
                continue
        elif x not in b:
            b.append(x)
        else:
            continue
    return sorted(a)+list(reversed(sorted(b[::-1])))
