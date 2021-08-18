t = int(input())
while t > 0:
    s = input()
    c = 0
    mx = 0
    d = 0
    for i in range(len(s)):
        c = 0
        if s[i] == '.' and s[i - 1] != '.':
            while s[i] != '
            c += 1
            i += 1
            if c > mx:
                d += 1
                mx = c
    print(d)
    t = t - 1
