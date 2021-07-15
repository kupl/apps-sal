
T = int(input())

for _ in range(T):
    H, W, a, b, = list(map(int, input().split()))

    if a * H != b * W:
        print("NO")
    else:
        print("YES")
        ans = [[0] * W for _ in range(H)]

        L = 0
        for y in range(H):
            for x in range(L, L + a):
                ans[y][x % W] = 1
            L += (W - a)

        for c in ans:
            print("".join(map(str, c)))

