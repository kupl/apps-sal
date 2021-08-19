t = int(input())
for i in range(t):
    s = input()
    d = {}
    min1 = len(s) + 1
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    l = [[x, y] for (x, y) in d.items()]
    l.sort(key=lambda j: j[1], reverse=True)
    for i in range(1, 26):
        f = len(s) // i
        c = 0
        if len(s) % i != 0:
            continue
        j = 0
        while j < i and j < len(l):
            if l[j][1] >= f:
                c += f
            else:
                c += l[j][1]
            j += 1
        c = len(s) - c
        if c < min1:
            min1 = c
    print(min1)
