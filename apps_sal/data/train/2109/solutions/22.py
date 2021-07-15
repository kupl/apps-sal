from math import ceil
Q = int(input())
AB = [list(map(int, input().split())) for i in range(Q)]

for a, b in AB:
    a, b = min(a, b), max(a, b)
    C = int((a*b)**0.5)
    if a == b:
        print(2*a-2)
        continue

    if a + 1 == b:
        print(2*a-2)
        continue

    if C**2 == a * b:
        C -= 1
    if C * (C+1) < a * b:
        print(2*C-1)
    else:
        print(2*C-2)
