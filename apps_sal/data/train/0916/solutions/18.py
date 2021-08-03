import math
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    val1 = n * m
    val2 = math.gcd(n, m)
    print(val1 // val2)
