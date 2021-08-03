# cook your dish here
t = int(input())
for _ in range(t):
    d = int(input())
    a = [int(i) for i in input().split()]
    c = 0
    for i in range(d):
        if a[i] >= d // 2:
            c += 1
    print(c)
