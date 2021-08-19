# cook your dish here
t = int(input())
while t > 0:
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    f = 0
    for i in a:
        if i >= x:
            f = 1
            break
    if f == 1:
        print("YES")
    else:
        print("NO")
    t = t - 1
