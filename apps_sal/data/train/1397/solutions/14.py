def bs(x, prev, pict):
    l = 0
    r = len(pict[x]) - 1
    while l <= r:
        if r - l < 5:
            for i in range(l, r + 1):
                if pict[x][i] > prev:
                    return pict[x][i]
            return -1
        mid = (l + r) // 2
        if pict[x][mid] < prev:
            l = mid + 1
        else:
            r = mid
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    li = []
    pict = {}
    for i in range(len(s)):
        if pict.get(s[i]) is None:
            pict[s[i]] = []
            li.append(s[i])
        pict[s[i]].append(i + 1)
    li.sort()
    count = 1
    prev = 0
    i=len(li)
    for i in range(len(li)):
        x = bs(li[i], prev, pict)
        if x != -1:
            prev = x
        else:
            count += 1
            prev = pict[li[i]][0]
    print(count)

