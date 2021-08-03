n, m, x = map(int, input().split())
while(n != 0 and m != 0 and x != 0):
    i = 0
    s = 0
    while(i < n):
        s += (x + i * (m)) // n
        i += 1
    print(s)
    n, m, x = map(int, input().split())
