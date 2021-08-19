def res(s):
    if len(s) == 2:
        if s[0] == s[1]:
            print('NO')
        else:
            print('YES')
    elif len(s) % 2 != 0:
        print('NO')
    else:
        counte = 0
        for i in range(2, len(s)):
            if i % 2 == 0:
                if s[i] != s[0]:
                    counte = 1
                    break
            elif s[i] != s[1]:
                counte = 1
                break
        if counte == 0:
            print('YES')
        else:
            print('NO')


def __starting_point():
    t = int(input())
    for _ in range(t):
        stri = str(input())
        res(stri)


__starting_point()
