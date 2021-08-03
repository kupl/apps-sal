for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    am = min(a)
    bm = min(b)
    ans = 0
    for i in range(n):
        ans += max(b[i] - bm, a[i] - am)
    print(ans)
