

t = int(input())


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


dp = {}


def solve(p, k, g, s, m, x, y, n):
    if ((p, k, g) in dp):
        return dp[(p, k, g)]

    ans = 0

    if (p == n):
        if k >= x and k <= y:
            ans = g
        else:
            ans = 0
    else:
        for i in range(p, n):

            if (i - p + 1 > m):
                break

            temp = solve(i + 1, k + 1, gcd(g, int(s[p:i + 1])), s, m, x, y, n)
            if (temp > ans):
                ans = temp

    dp[(p, k, g)] = ans
    return ans


while t != 0:
    dp = {}
    t -= 1
    n = int(input())
    s = input()
    m, x, y = list(map(int, input().split()))
    x += 1
    y += 1

    print(solve(0, 0, 0, s, m, x, y, n))
