import math
for i in range(int(input())):
    n = int(input())
    st = int(math.sqrt(n))
    mi = n
    for x in range(max(0, st - 100), st + 100):
        cur = ((n + x) // (x + 1)) + x - 1
        mi = min(cur, mi)
    print(mi)
