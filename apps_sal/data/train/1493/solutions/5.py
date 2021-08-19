for _ in range(int(input())):
    t = int(input())
    s = input()
    n = len(s)
    b = 0
    for i in s:
        if i == 'B':
            b += 1
    g = n - b
    if abs(b - g) > 1:
        print('-1')
    elif b == 1 and g == 1:
        print('0')
    elif b > g:
        BG = 'BG' * (n // 2)
        if n & 1:
            BG += 'B'
        (B, G) = ([], [])
        for i in range(n):
            if s[i] != BG[i]:
                if s[i] == 'B':
                    B.append(i)
                else:
                    G.append(i)
        if t == 0:
            print(len(B))
        else:
            print(sum([abs(B[i] - G[i]) for i in range(len(B))]))
    elif b < g:
        BG = 'GB' * (n // 2)
        if n & 1:
            BG += 'G'
        (B, G) = ([], [])
        for i in range(n):
            if s[i] != BG[i]:
                if s[i] == 'B':
                    B.append(i)
                else:
                    G.append(i)
        if t == 0:
            print(len(B))
        else:
            print(sum([abs(B[i] - G[i]) for i in range(len(B))]))
    else:
        BG = 'GB' * (n // 2)
        if n & 1:
            BG += 'G'
        (B, G) = ([], [])
        for i in range(n):
            if s[i] != BG[i]:
                if s[i] == 'B':
                    B.append(i)
                else:
                    G.append(i)
        if t == 0:
            v1 = len(B)
        else:
            v1 = sum([abs(B[i] - G[i]) for i in range(len(B))])
        BG = 'BG' * (n // 2)
        if n & 1:
            BG += 'B'
        (B, G) = ([], [])
        for i in range(n):
            if s[i] != BG[i]:
                if s[i] == 'B':
                    B.append(i)
                else:
                    G.append(i)
        if t == 0:
            v2 = len(B)
        else:
            v2 = sum([abs(B[i] - G[i]) for i in range(len(B))])
        print(min(v1, v2))
