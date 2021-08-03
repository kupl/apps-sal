import math

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [10 for _ in range(n)]
    mul = [1 for _ in range(n)]
    for i in range(m):
        s, e, t = list(map(int, input().split()))
        s = s - 1
        e = e - 1
        for j in range(s, e + 1):
            mul[j] *= t
    res = sum(mul) / len(mul)
    res = int(math.floor(res * 10))
    print(res)
