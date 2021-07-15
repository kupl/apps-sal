def part(n):
    p = sorted(set([prod(s) for s in parts(n)]))
    r = max(p) - min(p)
    a = sum(p) / float(len(p))
    m = (p[(len(p)-1)//2] + p[len(p)//2]) / 2.0
    return 'Range: {} Average: {:.2f} Median: {:.2f}'.format(r, a, m)
    
def prod(l):
    p = 1
    for i in l:
        p *= i
    return p
    
# http://jeromekelleher.net/generating-integer-partitions.html    
# No recursion
def parts(n):
    a = [0] * (n + 1)
    k = 1
    a[1] = n
    while k:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]
