from math import ceil
for _ in range(int(input())):
    n = int(input())
    x = (ceil((n ** 0.5)))
    if n <= x * (x - 1):
        print(x + x - 1 - 2)
    else:
        print(2 * x - 2)
