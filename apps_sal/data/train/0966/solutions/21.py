for _ in range(int(input())):
    (n, u, d) = map(int, input().split())
    H = list(map(int, input().split()))
    parachute = 1
    for i in range(n):
        if i == n - 1:
            break
        if H[i + 1] > H[i] and H[i + 1] - H[i] > u:
            break
        elif H[i + 1] < H[i] and H[i] - H[i + 1] > d:
            if parachute == 1:
                parachute = 0
                continue
            else:
                break
    print(i + 1)
