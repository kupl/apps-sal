T = int(input())
for i in range(T):
    l = list(map(int, input().split()))
    n, m = l[0], l[1]
    z = []
    distance = [0] * (m + n - 1)
    for i in range(n):
        arr = list(map(int, input()))
        for j, v in enumerate(arr):
            if v:
                z.append((i, j))
                for pt in z:
                    d = abs(pt[0] - i) + abs(pt[1] - j)
                    distance[d] += 1

    print(*distance[1:])
