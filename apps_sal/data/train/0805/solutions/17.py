t = int(input())
for _ in range(t):
    n = int(input())
    maxi = 0
    for i in range(n):
        (s, p, v) = [int(x) for x in input().split()]
        temp = p // (s + 1)
        temp = temp * v
        if maxi < temp:
            maxi = temp
    print(maxi)
