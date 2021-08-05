from math import gcd, ceil
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    gcdd = arr[0]
    for i in range(1, n):
        gcdd = gcd(arr[i], gcdd)
    print(gcdd, int(ceil(sum(arr) / gcdd)))
