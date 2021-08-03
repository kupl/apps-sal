import math
for t in range(int(input())):
    n = int(input())
    x = math.sqrt(n) - 1
    print(int(math.ceil(2 * x + 1)))
