import math
for _ in range(int(input())):
    n = int(input())
    x = int(math.sqrt(n))
    ans = n // x

    if(n % x != 0):
        ans += 1
    x -= 1
    ans += x
    print(ans - 1)
