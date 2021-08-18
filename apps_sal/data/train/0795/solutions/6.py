t = int(input())
while t > 0:
    n, k, l = map(int, input().split())
    if(k * l < n or (k == 1 and n > 1)):
        print("-1")
    else:
        for i in range(n):
            print((i % k) + 1, end=" ")
        print()
    t -= 1
