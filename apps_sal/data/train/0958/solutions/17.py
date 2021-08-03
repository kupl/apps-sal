def solve(n):
    if n == 1:
        print('*')
        return
    for i in range(1, n + 1):
        s = n - i
        p = '*'
        if 1 < i < n:
            m = 2 * i - 3
            p = p.ljust(m + 1)
            p += '*'
        elif i == n:
            t = 2 * i - 1
            p = p * t
        p = p.rjust(s + len(p))
        print(p)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        solve(n)


main()
