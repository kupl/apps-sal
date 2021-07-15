def inp():
    l = [0]*10
    for c in input():
        l[ord(c)-48] += 1
    return (l[0]+l[1]+l[2]+l[3], l[4], l[5]+l[6], l[7])

def go():
    a0,a4,a6,a7 = inp()
    b0,b4,b6,b7 = inp()
    r4 = r7 = 0
    m = min(b6, a7); r7 += m; b6 -= m; a7 -= m
    m = min(a6, b7); r7 += m; a6 -= m; b7 -= m
    m = min(b0, a7); r7 += m; b0 -= m; a7 -= m
    m = min(a0, b7); r7 += m; a0 -= m; b7 -= m
    m = min(b4, a7); r7 += m; b4 -= m; a7 -= m
    m = min(a4, b7); r7 += m; a4 -= m; b7 -= m
    m = min(a7, b7); r7 += m; a7 -= m; b7 -= m
    m = min(b0, a4); r4 += m; b0 -= m; a4 -= m
    m = min(a0, b4); r4 += m; a0 -= m; b4 -= m
    m = min(a4, b4); r4 += m; a4 -= m; b4 -= m
    print("7"*r7 + "4"*r4)

for t in range(eval(input())): go()

