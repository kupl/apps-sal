def loose_change(c, a):
    l, n = 0, 0
    s = sorted([a//i for i in c if i > 1 and a % i == 0])
    for i in range(len(c)-1, -1, -1):
        k = (a - l)//c[i]
        n += k
        if l + k * c[i] <= a:
            l += k * c[i]
    return min(n, s[0]) if s else n

