t = int(input())
while t > 0:
    (n, k) = map(int, input().split())
    y = list(map(int, input().split()))
    y.sort()
    k1 = []
    for i in range(len(y)):
        if i > k - 1:
            if y[i] != k1[-1]:
                break
            else:
                k1.append(y[i])
        else:
            k1.append(y[i])
    from itertools import combinations
    ans = list(combinations(k1, k))
    l = []
    for i in ans:
        l.append(sum(i))
    print(l.count(min(l)))
    t -= 1
