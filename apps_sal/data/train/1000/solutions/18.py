import math
t = int(input())
for i in range(t):
    a = int(input())
    val = input().split()
    val = [int(x) for x in val]
    ans = a / min(val)
    print(math.ceil(ans))
