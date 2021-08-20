def solve(n):
    if n == 1:
        print('0')
        return
    l = 3
    p1 = 1
    p2 = 1
    print('0')
    print('1 1')
    for i in range(n - 2):
        x = ''
        for i in range(l):
            nt = p1 + p2
            c = p2
            p2 = nt
            p1 = c
            x += str(nt)
            if i != l - 1:
                x += ' '
        print(x)
        l += 1


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        solve(n)


main()
