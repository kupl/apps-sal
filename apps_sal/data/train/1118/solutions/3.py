def intinp():
    return int(input())


def listinp(func=int):
    return list(map(func, input().split()))


def nsepline(n, func=str):
    return [func(input()) for _ in range(n)]


def printlist(li, glue=' '):
    return glue.join(list(map(str, li)))


for _ in range(intinp()):
    n = intinp()
    s = list(map(int, input()))
    nn = n + 1 if n & 1 == 1 else n
    x1 = '10' * nn
    x2 = '01' * nn
    c1 = c2 = 0
    for i in range(n):
        if s[i] != int(x1[i]):
            c1 += 1
        if s[i] != int(x2[i]):
            c2 += 1
    print(min(c1, c2))
