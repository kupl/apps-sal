for i in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
    else:
        n = n - 1
        ans = n * (n + 1) * (2 * n + 1) / 6
        print(int(ans))
