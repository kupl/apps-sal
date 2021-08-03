from math import factorial as fact
t = int(input())
while t > 0:
    n, k = map(int, input().split())
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
    c = k1[k - 1]
    ans = 0
    for i in range(k):
        if k1[i] == c:
            ans += 1
    ans2 = k1.count(c)
    print(fact(ans2) // (fact(ans) * fact(ans2 - ans)))

    t -= 1
