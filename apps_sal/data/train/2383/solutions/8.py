import math
for _ in range(int(input())):
    (a, b) = map(int, input().split())
    s = min(max(2 * a, b), max(2 * b, a))
    print(s ** 2)
