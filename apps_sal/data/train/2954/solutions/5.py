def riders(a):
    i = r = 0
    while i < len(a):
        n = next((k for k in range(i, len(a)) if sum(a[i:k + 1]) > 100), len(a))
        r += 1 ; i = n
    return r
