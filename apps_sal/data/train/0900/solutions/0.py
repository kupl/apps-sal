import math
t = int(input())
for i in range(t):
    k = int(input())
    res = pow(2, k, 1000000007) * 5 % 1000000007
    print(res)
