def sree(k, n):
    k.sort()
    l = [0, 0, 0]
    if k[n // 2] == k[(n // 2) - 1]:
        print(-1)
    else:
        l[1] = k[n // 2]
        if k[(3 * n) // 4] == k[(3 * n) // 4 - 1]:
            print(-1)
        else:
            l[2] = k[(3 * n) // 4]
            if k[n // 4] == k[(n // 4) - 1]:
                print(-1)
            else:
                l[0] = k[n // 4]
                print(l[0], l[1], l[2])


t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    sree(k, n)
