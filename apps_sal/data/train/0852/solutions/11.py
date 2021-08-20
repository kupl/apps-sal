def fk(s: str):
    s = int(s)
    t = 0
    ini = 0
    q = 1
    for i in range(1, s * s + 1):
        print(ini, end='')
        ini = 1 - ini
        t += 1
        if t == s:
            q += 1
            print()
            t = 0
            if q % 2 == 0:
                ini = 1
            else:
                ini = 0


n = input()
n = int(n)
t = [fk(input()) for i in range(n)]
