for _ in range(int(input())):
    n = int(input())
    a = [*list(map(int, input().split()))]
    ans = 100000000000000000000
    for i in range(0, len(a) - 1):
        mn = a[i] - a[i + 1]
        if mn < ans:
            ans = mn
    print(ans)
