for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    md = {}
    for i in range(n):
        s, e, p = list(map(int, input().split()))
        if p in md:
            md[p].append((s, e))
        else:
            md[p] = [(s, e)]
    sm = 0
    for i in range(k):
        if i + 1 in md:
            md[i + 1].sort(key=lambda x: x[1])
            c = 1
            curr = md[i + 1][0][1]
            for x in md[i + 1]:
                if x[0] >= curr:
                    curr = x[1]
                    c += 1
            sm += c
    print(sm)
