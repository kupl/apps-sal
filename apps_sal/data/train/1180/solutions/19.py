t = int(input())
for a in range(t):
    (n, k, x, y) = map(int, input().split())
    if x == y:
        print(n, n)
    else:
        temp = []
        if x > y:
            temp = [[n, n - x + y], [n - x + y, n], [0, x - y], [x - y, 0]]
        else:
            temp = [[n + x - y, n], [n, n - y + x], [y - x, 0], [0, y - x]]
        ans = temp[(k - 1) % 4]
        print(*ans)
