t = int(input())
for i in range(t):
    n = int(input())
    d = n % 10
    if d == 0:
        print(0)
    elif d == 5:
        print(1)
    else:
        print(-1)
