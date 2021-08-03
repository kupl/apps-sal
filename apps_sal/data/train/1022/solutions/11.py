
t = int(input())
for _ in range(t):
    n = int(input())
    dist = list(map(int, input().split()))
    if n % 2 != 0:
        print("NO")
    else:
        f = 1
        for i in range(n // 2):
            if dist[i] != dist[i + n // 2] and dist[i] != -1 and dist[i + n // 2] != -1:
                f = 0
                break
            elif dist[i] == -1 and dist[i + n // 2] == -1:
                dist[i] = 1
                dist[i + n // 2] = 1

            else:
                dist[i] = dist[i + n // 2] = max(dist[i], dist[i + n // 2])

        if f == 0:
            print("NO")
        else:
            print("YES")
            print(' '.join(map(str, dist)))
