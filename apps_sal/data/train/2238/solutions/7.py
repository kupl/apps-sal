def f():
    (l, r) = map(int, input().split())
    if l == r:
        return l
    (a, b) = (bin(l)[2:], bin(r)[2:])
    (i, k) = (0, len(b))
    a = a.zfill(k)
    while a[i] == b[i]:
        i += 1
    d = k - i
    if b[i:].count('1') == d:
        return r
    return (r >> d << d) + (1 << d - 1) - 1


for i in range(int(input())):
    print(f())
