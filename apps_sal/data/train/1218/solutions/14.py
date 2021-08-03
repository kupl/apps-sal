n = int(input())
for j in range(n):
    x = [int(y) for y in input().split(' ')]
    if(x[1] % x[0] == 0):
        x[1] = x[1] - 1
    p = x[1] // x[0]
    p = p * x[0]
    print(p * (x[0] + p) // (x[0] * 2))
