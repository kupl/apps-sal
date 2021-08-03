def main():
    while True:
        n, m, x = map(int, input().split())
        if [n, m, x] == [0, 0, 0]:
            break

        ans = 0
        for k in range(1111):
            l = ((k * m - x + n - 1) // n)
            r = ((((k + 1) * m - x + n - 1) // n) - 1)

            l = max(l, 0)
            r = min(r, m - 1)

            if l < m and 0 <= r and l <= r:
                ans += k * (r - l + 1)

        print(ans)


main()
