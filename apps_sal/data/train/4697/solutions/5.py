def common(a,b,c): 
    a.sort() ; b.sort() ; c.sort()
    i = j = k = c1 = 0
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            c1 += a[i]
            i += 1 ; j += 1 ; k += 1
        elif a[i] < b[j] : i += 1
        elif b[j] < c[k] : j += 1
        else : k += 1
    return c1
