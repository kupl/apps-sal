# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    s = ''
    while n > 0:
        s += input()
        n -= 1
    c = s.count('c')
    c = c // 2
    o = s.count('o')
    d = s.count('d')
    e = s.count('e')
    e = e // 2
    h = s.count('h')
    f = s.count('f')
    m = min(c, o, d, e, h, f)
    print(m)
    t -= 1
