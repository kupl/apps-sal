import math
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    div = sum(a) / n
    div = math.ceil(div)
    count = div * n - sum(a)
    for i in a:
        if i > div:
            count += i - div
    print(count)
