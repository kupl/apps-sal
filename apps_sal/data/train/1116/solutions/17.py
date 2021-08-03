# cook your dish here
try:
    n = int(input())
    a = list(map(int, input().split()))

    sums = {}
    cur = 0
    cnt = 0

    for i in range(n):
        cur += a[i]

        if cur == 0:
            cnt += 1
        if cur in sums:
            cnt += sums[cur]

        sums[cur] = 1 if cur not in sums else sums[cur] + 1

    print(cnt)
except:
    pass
