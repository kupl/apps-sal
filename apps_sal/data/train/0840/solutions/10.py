def solve(n):
    if n == 1:
        print('*')
        return
    s = 0
    ms = n // 2
    o = 1
    for i in range(n):
        if s == ms:
            o = -1
        x = '*'
        x = x.rjust(1 + s)
        s += o
        print(x)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        solve(n)


main()
