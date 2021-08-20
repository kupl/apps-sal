import math
T = int(input())
for t in range(T):
    s = set()
    n = int(input())
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n / i)
    if len(s) % 2 != 0:
        print('YES')
    else:
        print('NO')
