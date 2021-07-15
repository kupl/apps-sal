def solve(a):
    n = len(a)
    for i in range(n-1):
        if a[i] in a[i+1:]: a[i] = 'a'
    while True:
        if 'a' in a: a.remove('a')
        else     : break
    return a

