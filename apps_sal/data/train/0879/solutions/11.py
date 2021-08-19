# cook your dish here
t = int(input())
for i in range(0, t):
    x, y = map(int, input().split())
    s = 0
    b = []
    for j in range(1, 10):
        b.append((y * j) % 10)
    if(x // y) < 10:
        for j in range(0, x // y):
            s += b[j]
    else:
        s += ((x // y) // 10) * sum(b)
        for j in range(0, (x // y) % 10):
            s += b[j]
    print(s)
