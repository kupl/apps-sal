N = int(input())
l = []
for i in range(N):
    l.append(input())
for j in range(N-1,-1,-1):
    s = '` '+ l[j]
    n = len(s)-1
    y = s[n]
    f = ''
    while y != '`':
        w = ''
        while y != ' ':
            if ord(y) in range(97,123) or ord(y) in range(65,91):
                w += y
            n -= 1
            y = s[n]
        wf = ''
        n -= 1
        y = s[n]
        x = len(w)
        for k in range(x):
            wf += w[x-k-1]
        f += wf+' '
    print(f)
