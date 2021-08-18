from math import floor, sqrt
for _ in range(int(input())):
    n = int(input())

    x = floor(sqrt(n / 2))
    print(x * 2)
