def even_numbers(arr,n):
    s = []
    for e in arr:
        if e%2 == 0:
            s.append(e)
    s1 = s[:-n-1:-1]
    s2 = s1[::-1]
    return s2
