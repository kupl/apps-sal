t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    weightlist = list(map(int, input().split()))
    summofweights = 0
    sonweight = 0
    dadweight = 0
    weightlist.sort()
    for j in weightlist:
        summofweights += j
    if k > n / 2:
        for j in range(-1, -(k + 1), -1):
            dadweight += weightlist[j]
        ans = False
    else:
        for j in range(k):
            sonweight += weightlist[j]
        ans = True
    if ans:
        print(summofweights - 2 * sonweight)
    else:
        print(2 * dadweight - summofweights)
