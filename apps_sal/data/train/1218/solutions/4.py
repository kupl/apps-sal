t = int(input())
for i in range(t):
    x, n = input().split()
    x = int(x)
    n = int(n)
    s = 0
    for j in range(x,n,x):
        s = s + j
    print(s)

