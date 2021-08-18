for _ in range(int(input())):
    n, u, d = map(int, input().split())
    h = list(map(int, input().split()))
    b = 0
    for i in range(n):
        if i == n - 1:
            break
        if h[i + 1] > h[i]:
            if h[i + 1] - h[i] > u:
                break
        elif h[i + 1] < h[i]:
            if h[i] - h[i + 1] > d:
                if b == 0:
                    b = 1
                else:
                    break
    print(i + 1)
