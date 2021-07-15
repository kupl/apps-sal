import math
for _ in range(int(input())):
    n = int(input())
    grid = [int(i) for i in input().split()]
    sum1 = int('1'*n)*sum(grid)*math.factorial(n-1)
    print(sum1)

