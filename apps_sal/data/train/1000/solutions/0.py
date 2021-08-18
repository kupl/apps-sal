from math import ceil
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = ceil(n / min(a))
    print(int(ans))
