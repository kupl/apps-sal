import math
for _ in range(int(input())):
    (a, b) = [int(i) for i in input().split()]
    ans = 1
    sum = 0
    c = int(math.log2(a))
    for i in range(c + 1):
        doo = 2 ** i
        po = doo & a
        if po == doo:
            sum += min(b - a + 1, ans) * doo
        else:
            ans += doo
    print(sum % 1000000007)
