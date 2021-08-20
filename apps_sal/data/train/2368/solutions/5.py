for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a1 = min(a)
    b1 = min(b)
    ans = 0
    for i in range(n):
        (cnt1, cnt2) = (a[i] - a1, b[i] - b1)
        ans += max(cnt1, cnt2)
    print(ans)
