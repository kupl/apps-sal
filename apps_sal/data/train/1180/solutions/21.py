t = int(input())
for _ in range(t):
    (n, k, x, y) = map(int, input().split())
    if x == y:
        print(n, n)
    else:
        temp = []
        if x > y:
            temp = [[n, y + n - x], [y + n - x, n], [0, x - y], [x - y, 0]]
        else:
            temp = [[x + n - y, n], [n, n - y + x], [y - x, 0], [0, y - x]]
        ans = temp[(k - 1) % 4]
        print(*ans)
