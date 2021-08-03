for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    m = l1[-1]
    ans = 0
    for i in range(-2, -n - 1, -1):
        if l1[i] > m:
            ans += 1
        else:
            m = l1[i]
    print(ans)
