# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    f = list(map(int, input().split()))
    d = 0
    for i in f:
        if i >= x:
            d = 1
            break
    if d == 1:
        print("YES")
    else:
        print("NO")
