def show(n, d):
    t = 0
    m = 1000000007
    for i in range(0, n):
        t = t * 10 + d
    t = t * t
    st = str(t)
    s = 0
    for i in range(0, len(st)):
        s = (s + 23 ** i * int(st[i]) % m) % m
    print(s)


def main():
    t = int(input())
    while t > 0:
        (n, d) = input().split()
        n = int(n)
        d = int(d)
        show(n, d)
        t -= 1


main()
