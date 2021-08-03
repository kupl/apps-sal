import math
for _ in range(int(input())):
    n = int(input()) - 1
    nth = math.pow(n, 2) + math.pow((n + 1), 3)
    print(int(nth % 1000000007))
