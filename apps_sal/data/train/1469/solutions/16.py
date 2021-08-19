# cook your dish here

# t = [input() for i in range(n)]


def fk(s: str):
    s = int(s)
    for i in range(2, 1 + 1 + int(s)):
        for k in range(i, i + s):
            print(k, end='')
        print()
    # t = 0
    # for i in range(1, s*s+1):
    #     print(i*2, end='')
    #     t += 1
    #     if t == s:
    #         print()
    #         t = 0


n = input()
n = int(n)
t = [fk(input()) for i in range(n)]

# fk(3)
