for __ in range(int(input())):
    n = int(input())
    ans = 10 ** 9
    for i in range(1, min(n, 10 ** 5)):
        ans = min(i - 1 + (n - 1) // i, 10 ** 6, ans)
    if ans == 10 ** 9:
        ans = 0
    print(ans)
