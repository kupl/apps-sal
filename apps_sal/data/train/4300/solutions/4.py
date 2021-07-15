def solve(a, b):
    if a[0] in b:
        if len(a) > 1:
            return solve(a[1:],b[b.index(a[0])+1:])+solve(a,b[b.index(a[0])+1:])
        else:
            print((b.count(a)))
            return b.count(a)
    else:
        return 0

    

