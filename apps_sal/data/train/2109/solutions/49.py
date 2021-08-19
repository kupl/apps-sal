import math
Q = int(input())
Query = []
for i in range(Q):
    Query.append(tuple(map(int, input().split())))
for (a, b) in Query:
    sq = int(math.sqrt(a * b))
    ans = sq * 2 - 1
    if a == b:
        ans -= 1
    elif sq ** 2 == a * b:
        ans -= 2
    elif sq * (sq + 1) >= a * b:
        ans -= 1
    print(ans)
