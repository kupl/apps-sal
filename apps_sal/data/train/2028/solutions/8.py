def pallin(s):
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def __starting_point():
    s = input()
    n = len(s)
    for i in range(n - 1, 0, -1):
        s1 = s[0:i]
        s2 = s[i:]
        t = s2 + s1
        if s != t and pallin(t):
            print('1')
            return
    for i in range(1, n // 2):
        if s[i] != s[i - 1]:
            print('2')
            return
    print('Impossible')


__starting_point()
