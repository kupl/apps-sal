import math

t = int(input())
for i in range(t):
    n = int(input())
    sq = int(math.sqrt(n))
    if sq * sq == n:
        print("YES")
    else:
        print("NO")
