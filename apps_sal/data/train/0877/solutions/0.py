t = int(input())
for _ in range(t):
    x, y, k, n = [int(x) for x in input().split()]
    k = k * 2
    temp = abs(x - y)
    if(temp % k == 0):
        print("Yes")
    else:
        print("No")
