import math
t = eval(input())
while t:
    n = eval(input())
    if n % 2 == 0:
        x = pow(3, n, 1000000007)
        x = x + 3
        print(x)
    else:
        x = pow(3, n, 1000000007)
        x = x - 3
        print(x)
    t = t - 1
