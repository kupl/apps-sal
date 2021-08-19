T = int(input())
res = []
for i in range(T):
    a = input()
    a = list(a.split())
    s = int(a[0])
    w1 = int(a[1])
    w2 = int(a[2])
    w3 = int(a[3])
    b = 0
    hits = 0
    if w1 + w2 <= s:
        if w1 + w2 + w3 <= s:
            hits += 1
        else:
            hits += 2
    elif w1 + w2 > s:
        if w1 <= s:
            hits += 1
        if w2 + w3 > s:
            if w2 <= s:
                hits += 2
            else:
                hits += 1
        else:
            hits += 1
    b = hits
    hit = 0
    if w3 + w2 <= s:
        if w1 + w2 + w3 <= s:
            hit += 1
        else:
            hit += 2
    elif w3 + w2 > s:
        if w3 <= s:
            hit += 1
        if w2 + w1 > s:
            if w2 <= s:
                hit += 2
            else:
                hit += 1
        else:
            hit += 1
    if b > hit:
        b = hit
    res.append(b)
for num in res:
    print(num)
