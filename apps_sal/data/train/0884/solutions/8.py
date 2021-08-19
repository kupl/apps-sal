import math
for _ in range(int(input())):
    (x, k) = map(int, input().split())
    a = {x}
    b = {k}
    for i in range(2, int(math.sqrt(max(x, k)) + 2)):
        if i <= x and x % i == 0:
            a.add(i)
            a.add(int(x / i))
        if i <= k and k % i == 0:
            b.add(i)
            b.add(int(k / i))
    ans1 = 0
    ans2 = 0
    for i in a:
        if i != 1:
            ans1 += pow(i, k)
    for i in b:
        if i != 1:
            ans2 += i * x
    print(ans1, end=' ')
    print(ans2)
