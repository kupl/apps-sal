t = int(input())
for _ in range(t):
    n = int(input())
    maxi = 0
    for i in range(n):
        k = int(input())
        if k > maxi:
            maxi = k
    print(maxi)
