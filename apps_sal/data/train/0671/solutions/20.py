t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = y = 101
    for i in range(n):
        if a[i] == 0:
            x = min(x, c[i])
            if s + x + y <= 100:
                print("yes")
                break
        else:
            y = min(y, c[i])
            if s + x + y <= 100:
                print("yes")
                break
    else:
        print("no")
