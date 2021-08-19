import math
t = int(input())
for _ in range(t):
    x, y, k = list(map(int, input().split()))
    s = x + y
    if s % k == 0:
        if (s // k) % 2 == 0:
            print("Chef")
        else:
            print("Paja")
    else:
        if math.ceil(s / k) % 2 == 0:
            print("Paja")
        else:
            print("Chef")  # cook your dish here
