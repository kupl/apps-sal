def solve(n):
    c = 1
    r = list(range(1, n + 1))
    r.sort(reverse=True)
    for i in r:
        x = ''
        for j in range(i):
            x += str(c)
            c += 1
        print(x)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        solve(n)


main()
