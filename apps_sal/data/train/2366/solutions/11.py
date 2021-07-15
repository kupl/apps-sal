for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans, min1 = 0, float('inf')
    for q in range(n-1, -1, -1):
        if a[q] > min1:
            ans += 1
        min1 = min(min1, a[q])
    print(ans)

