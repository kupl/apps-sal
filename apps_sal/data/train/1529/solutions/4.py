import math
T = int(input())
for i in range(T):
    N = int(input())
    list = input().split()
    s = 0
    k = '0'
    for j in range(N):
        list[j] = int(list[j])
        s += list[j]
    for l in range(N):
        k = k + '1'
    k = int(k)
    c = math.factorial(N - 1)
    print(s * c * k)
