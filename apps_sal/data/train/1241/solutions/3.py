# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    e = 0
    o = 0
    for i in a:
        if(i % 2 == 0):
            e = e + 1
        else:
            o = o + 1
    if (e <= x // 2):
        flag = (n - x + 1) % 2

    elif (o <= x // 2):
        flag = 1

    else:
        flag = (x + 1) % 2

    if (flag == 1):
        print("Jesse")
    else:
        print("Walter")
