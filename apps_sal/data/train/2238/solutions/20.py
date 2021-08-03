n = int(input())
for j in range(0, n):
    l, r = map(int, input().split(" "))
    while(l | (l + 1) <= r):
        l = l | (l + 1)
    print(l)
