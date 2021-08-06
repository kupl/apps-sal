n, x, y = map(int, input().split())
l = list(map(int, input().split()))
c = 0
for i in l:
    c += x
    if i == 1:
        c += y
    else:
        t = (i - 1) * (y * 2 / 100)
        if y - t > 0:
            c += y - t
    if c >= 300:
        print("YES")
        break
else:
    print("NO")
