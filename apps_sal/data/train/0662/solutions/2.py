# cook your dish here
def __starting_point():
    for _ in range(int(input())):
        d = int(input())
        l, r = map(int, input().split())
        if l % 2 != 0:
            l -= 1
        if r % 2 != 0:
            r += 1
        n = (r - l) // (2 * d)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2 + 1
        a = d * (l + d)
        f = 4 * d * d
        ans = ((n * (2 * a + (n - 1) * f)) // 2) % 1000000007
        print(ans)


__starting_point()
