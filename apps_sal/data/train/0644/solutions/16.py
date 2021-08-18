t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))[:n]
    z = sum(l)
    if(z % n == 0):
        print("Yes")
    else:
        print("No")
