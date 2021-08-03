def f(n):
    s = list(input().strip())
    mina = len([x for x in s if x == 'a'])
    ln = len(s)
    minb = ln - mina
    for i in range(n - 1):
        s = list(input().strip())
        curra = len([x for x in s if x == 'a'])
        currb = len([x for x in s if x == 'b'])
        if mina > curra:
            mina = curra
        if minb > currb:
            minb = currb
    return min(mina, minb)


t = int(input())
for i in range(t):
    n = int(input())
    print(f(n))
