for t in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= a[i] - i
        ans %= 10 ** 9 + 7
        if ans == 0:
            break
    print(ans)
