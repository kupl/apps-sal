from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    d = defaultdict(list)
    for i in range(n):
        d[arr[i]].append(i + 1)
    ind = -10**10
    uno = list(set(arr))
    uno.sort()
    for i in uno:
        f = 0
        f2 = 0
        k = 0
        op = d[i]
        for j in op:
            if f2 == 0:
                f2 = 1
                ck = j
            if j > ind:
                ind = j
                f = 1
                break
        if f == 0:
            ind = ck
            ans += 1
    print(ans)
