for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = 0
    s2 = 0
    ans = 0
    for i in range(n):
        if a[i] == b[i] and s1 == s2:
            ans += a[i]
        s1 += a[i]
        s2 += b[i]
    print(ans)
