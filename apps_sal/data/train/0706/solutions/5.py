t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    w = list(map(int, input().split()))

    p = 0
    ans = 0
    flag = False
    while p < n:
        pick = 0
        if w[p] > k:
            flag = True
            break
        else:
            while p < n:
                if pick + w[p] <= k:
                    pick += w[p]
                    p += 1
                else:
                    break
            ans += 1
            pick = 0

    if flag:
        print(-1)
    else:
        print(ans)
