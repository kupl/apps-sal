def solve(a):
    a.sort()
    i,j= 1,0
    while j < len(a):
        j += 1
        if a[j-1] <= i:
            i += a[j-1]
        else: 
            break
    return i
