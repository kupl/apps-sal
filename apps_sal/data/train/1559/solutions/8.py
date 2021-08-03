t = int(input())
for i in range(t):
    n = int(input())
    if n & 1 == 0:
        print(pow(3, n, 1000000000 + 7) + 3)
    else:
        print(pow(3, n, 1000000000 + 7) - 3)
