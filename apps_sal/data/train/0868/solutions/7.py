for _ in range(int(input())):
    (n, k) = map(int, input().split())
    from math import ceil
    l = [int(i) for i in input().split()]
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            add = ceil(k / (j - i + 1))
            curr = l[i:j + 1]
            curr.sort()
            if k <= j - i + 1:
                x = curr[k - 1]
            else:
                x = curr[ceil(k / add) - 1]
            z = curr.count(x)
            if z in curr:
                cnt += 1
    print(cnt)
