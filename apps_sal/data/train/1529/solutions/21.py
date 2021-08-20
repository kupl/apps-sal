import math
t = int(input())
while t > 0:
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    summ = 0
    for i in range(0, n):
        summ += math.pow(10, i)
    summ = sum(a) * summ * math.factorial(n - 1)
    print(int(summ))
    t -= 1
