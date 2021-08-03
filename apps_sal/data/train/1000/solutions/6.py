import math
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(math.ceil(n / min(l)))
