import math
T = int(input())
while T:
    a, b = map(int, input().split())
    if math.gcd(a, b) == 1:
        print("YES")
    else:
        print("NO")
    T -= 1
