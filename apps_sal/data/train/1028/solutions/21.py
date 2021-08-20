def check(n):
    s = str(n)
    l = len(s)
    add = 0
    for i in range(l):
        add = add + int(s[i]) ** l
    if add == n:
        return 1
    else:
        return 0


def __starting_point():
    for _ in range(int(input())):
        n = int(input())
        if check(n):
            print('FEELS GOOD')
        else:
            print('FEELS BAD')


__starting_point()
