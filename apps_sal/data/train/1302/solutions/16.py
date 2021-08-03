from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    room = int(sqrt(n // 2))
    print(room * 2)
