def fk(s: str):
    s = int(s)
    res = ''
    ini = 1
    for i in range(s):
        res += str(ini)
        ini = 1 - ini
    for i in range(s):
        print(res)


n = eval(input())
n = int(n)
t = [fk(eval(input())) for i in range(n)]
