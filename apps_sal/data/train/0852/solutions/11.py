# cook your dish here

# t = [input() for i in range(n)]


def fk(s: str):
    s = int(s)
    # for i in range(2, 1+1+int(s)):
    #     for k in range(i, i+s):
    #         print(k, end='')
    #     print()

    t = 0
    ini = 0
    q = 1
    for i in range(1, s*s+1):
        print(ini, end='')
        ini = 1-ini
        t += 1
        if t == s:
            q += 1
            print()
            t = 0
            if q % 2 == 0:
                ini = 1
            else:
                ini = 0

    # res = ''
    # ini = 1
    # for i in range(s):
    #     res += str(ini)
    #     ini = 1-ini
    # for i in range(s):
    #     print(res)


n = input()
n = int(n)
t = [fk(input()) for i in range(n)]

# fk(5)

