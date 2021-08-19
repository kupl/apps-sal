t = int(input())
for i in range(t):
    n = int(input())
    h = 0
    while n > h:
        h = h + 1
        n = n - h
    print(h)
