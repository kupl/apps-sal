import math
t = eval(input())
for i in range(t):
    b = []
    (h, s) = list(map(int, input().split()))
    a = math.pow(h, 4) - 16 * s * s
    if a < 0:
        print('-1')
    else:
        ans = math.sqrt(a)
        answe = (h * h + ans) / 2
        answe2 = (h * h - ans) / 2
        if answe > 0:
            b.append(math.sqrt(answe))
            b.append(2 * s / b[0])
        ' \n     if(answe2>0):\n      c.append(math.sqrt(answe2))\n      c.append((2*s)/c[0])\n     '
        b.sort()
        print(str(b[0]) + ' ' + str(b[1]) + ' ' + str(h))
