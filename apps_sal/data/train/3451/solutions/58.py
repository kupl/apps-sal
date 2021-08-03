def triangle(k):
    s = ''
    if len(k) == 1:
        return k
    for i in range(len(k) - 1):
        if k[i] == k[i + 1]:
            s += k[i]
        elif (k[i] == 'R' and k[i + 1] == 'B') or (k[i] == 'B' and k[i + 1] == 'R'):
            s += 'G'
        elif (k[i] == 'R' and k[i + 1] == 'G') or (k[i] == 'G' and k[i + 1] == 'R'):
            s += 'B'
        elif (k[i] == 'G' and k[i + 1] == 'B') or (k[i] == 'B' and k[i + 1] == 'G'):
            s += 'R'
    print(s)
    while len(s) > 0:
        if len(s) == 1:
            return s
        s1 = s
        s = ''
        for i in range(len(s1) - 1):
            if s1[i] == s1[i + 1]:
                s += s1[i]
            elif (s1[i] == 'R' and s1[i + 1] == 'B') or (s1[i] == 'B' and s1[i + 1] == 'R'):
                s += 'G'
            elif (s1[i] == 'R' and s1[i + 1] == 'G') or (s1[i] == 'G' and s1[i + 1] == 'R'):
                s += 'B'
            elif (s1[i] == 'G' and s1[i + 1] == 'B') or (s1[i] == 'B' and s1[i + 1] == 'G'):
                s += 'R'
