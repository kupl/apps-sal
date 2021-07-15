def solve(n):
    a=[1]
    for _ in range(n-1):
        b=[1]
        for x in a[1:]:
            b.append(x+b[-1])
        b.append(b[-1])
        a=b
    return sum(a)
