# cook your dish here
for i in range(int(input())):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if i >= x:
            c += 1
    if c >= 1:
        print("YES")
    else:
        print("NO")
