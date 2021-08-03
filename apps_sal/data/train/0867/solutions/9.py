# cook your dish here
t = int(input())
for _ in range(t):
    a = [int(x) for x in input().split()]
    q = 0
    c = 0
    for i in range(1, 4):
        if(q + a[i] <= a[0]):
            q = q + a[i]
            c += 1
        else:
            q = 0
    if(c == 0):
        print(1)
    else:
        print(c)
