for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    ans = 0
    x = l[k - 1]
    for i in range(n):
        if x > l[i]:
            break
        ans += 1
    print(ans)
