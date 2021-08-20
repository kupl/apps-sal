t = int(input())
while t > 0:
    n = int(input())
    li = []
    (c, o, d, e, h, f) = (0, 0, 0, 0, 0, 0)
    for i in range(0, n):
        s = input()
        for i in range(len(s)):
            if s[i] == 'c':
                c = c + 1
            elif s[i] == 'o':
                o = o + 1
            elif s[i] == 'd':
                d = d + 1
            elif s[i] == 'e':
                e = e + 1
            elif s[i] == 'h':
                h = h + 1
            elif s[i] == 'f':
                f = f + 1
    e = e // 2
    c = c // 2
    print(min(c, o, d, e, h, f))
    t -= 1
