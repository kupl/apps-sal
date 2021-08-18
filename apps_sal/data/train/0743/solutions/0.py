t = int(input())
for i in range(t, 0, -1):
    x, y = map(int, input().split())
    k = x // y

    if k % y == 0:
        print("NO")
    else:
        print("YES")
