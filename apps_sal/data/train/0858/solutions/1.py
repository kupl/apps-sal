from math import log
t = int(input())
for _ in range(t):
    k = int(input())
    print(pow(2, int(log(k, 2))))
