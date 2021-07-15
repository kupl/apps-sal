# cook your dish here

# t = [input() for i in range(n)]


def fk(s: str):
    s = int(s)
    # for i in range(2, 1+1+int(s)):
    #     for k in range(i, i+s):
    #         print(k, end='')
    #     print()
    # t = 0
    # for i in range(1, s*s+1):
    #     print(i*2, end='')
    #     t += 1
    #     if t == s:
    #         print()
    #         t = 0
    res = ''
    ini = 1
    for i in range(s):
        res += str(ini)
        ini = 1-ini
    for i in range(s):
        print(res)


n = eval(input())
n = int(n)
t = [fk(eval(input())) for i in range(n)]

# fk(3)

