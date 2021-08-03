for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    ans = []
    sign = -1
    for ansi in range(n, 0, -1):
        if (a[(n + ansi * sign) // 2] == b[ansi - 1]) ^ (sign > 0):
            ans.append(1)
        ans.append(ansi)
        sign = -sign
    print(len(ans), *ans)
