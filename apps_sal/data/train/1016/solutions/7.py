# cook your dish here
t = int(input())
for z in range(t):
    n = int(input())
    c = 0
    for i in range(n):
        s, j = [int(x) for x in input().split()]
        if j - s > 5:
            c += 1
    print(c)
