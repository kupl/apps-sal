import math
for _ in range(int(input())):
    n = int(input())
    layers = [int(x) for x in input().split()]
    times = math.factorial(n - 1)
    d = sum(layers) * times
    ans = 0
    k = 1
    for i in range(n):
        ans += k * d
        k *= 10
    print(ans)
