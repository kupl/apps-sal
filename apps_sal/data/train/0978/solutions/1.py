import math
for i in range(int(input())):
    n = int(input())
    if n <= 2 or n > 1000000007:
        print('0')
    else:
        print(math.factorial(n - 1) * (math.factorial(n) - 2) % 1000000007)
