for i in range(int(input())):
    s = input()
    m = 0
    p = 0
    d = 0
    l = []
    for i in range(len(s)):
        if s[i] == '.':
            m = m + 1
        elif s[i] == '#':
            l.append(m)
            m = 0
    for i in range(len(l)):
        if l[i] > p:
            p = l[i]
            d = d + 1
    print(d)
