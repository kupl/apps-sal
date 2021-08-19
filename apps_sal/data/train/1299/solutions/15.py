t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    d = dict.fromkeys(set(lst), 0)
    d[lst[0]] = 1
    lst[0] *= -1
    for i in range(1, len(lst)):
        if lst[i] != -1 * lst[i - 1]:
            d[lst[i]] += 1
            lst[i] *= -1
    resl = []
    mx = 0
    k = 0
    for i in d:
        if d[i] > mx:
            mx = d[i]
    for i in d:
        if d[i] == mx:
            resl.append(i)
    print(min(resl))
