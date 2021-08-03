def main():
    pwd = input()
    n = int(input())
    f_l = False
    s_l = False
    for _ in range(n):
        b = input()
        if b == pwd:
            print('YES')
            return
        if pwd[1] == b[0]:
            f_l = True
        if pwd[0] == b[1]:
            s_l = True
    if f_l and s_l:
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
