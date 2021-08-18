import decimal
from decimal import *


def solve(a, b, min1, min2, min3, min4, x, y):
    if a > b:
        return []
    solMin1 = (a / y + b) / (y - 1 / y)
    solMin2 = (b / y + a) / (y - 1 / y)
    solMin1 *= (x * y)
    solMin2 *= (x * y)

    if solMin1 >= min1 and solMin1 <= min2 and solMin2 >= min3 and solMin2 <= min4:
        return [a, solMin1, b, solMin2]
    return []


def integerPart(x):
    return Decimal(str(x).split(".")[0])


def fractionalPart(x):
    t = str(x).split(".")
    if len(t) > 0:
        return "." + t[1]
    return 0


getcontext().prec = 30
for i in range(eval(input())):
    (x, y) = input().split()
    (a, b, c, d, e, f, g, h) = input().split()
    x = Decimal(x)
    y = Decimal(y)
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    d = Decimal(d)
    e = Decimal(e)
    f = Decimal(f)
    g = Decimal(g)
    h = Decimal(h)

    if a > g or (a == g and b > h):
        print("-1")
        continue

    solutionh = Decimal("-1")
    solutionm = Decimal("-1")
    diff = Decimal("-10000000000000000")

    solution1 = []
    solution2 = []
    solution3 = []
    solution4 = []
    solution5 = []
    solution6 = []
    solution7 = []
    solution8 = []
    solution9 = []
    solution10 = []
    solution11 = []
    solution12 = []
    solution13 = []
    solution14 = []
    l1 = 0
    if g == e:
        l1 = f
    solution1 = solve(a + 0, g + 0, b, x * y, l1, h, x, y)
    if a < y - 1 and len(solution1) == 0:
        solution2 = solve(a + 1, g + 0, 0, x * y, l1, h, x, y)
    if g >= 1 and len(solution1) == 0 and len(solution2) == 0:
        solution4 = solve(a + 0, g - 1, b, x * y, 0, x * y, x, y)
    if g - e >= 2 and c - a >= 2:
        solution5 = solve(a + 1, g - 1, 0, x * y, 0, x * y, x, y)

    if len(solution1) == 0 and len(solution2) == 0 and len(solution4) == 0:
        solution10 = solve(a, e, 0, x * y, 0, x * y, x, y)
        solution11 = solve(c, e, 0, x * y, 0, x * y, x, y)
        solution12 = solve(c, g, 0, x * y, 0, x * y, x, y)
    if a < y - 1 and len(solution1) == 0 and len(solution2) == 0 and len(solution4) == 0 and c - a >= 2:
        solution13 = solve(a + 1, e, 0, x * y, 0, x * y, x, y)
    if g >= 1 and len(solution1) == 0 and len(solution2) == 0 and len(solution4) == 0 and g - e >= 2:
        solution14 = solve(c, g - 1, 0, x * y, 0, x * y, x, y)

    if len(solution1) > 0:
        if solution1[0] < c or (solution1[0] == c and solution1[1] <= d):
            if solution1[2] > e or (solution1[2] == e and solution1[3] >= f):
                t = (solution1[2] - solution1[0]) * x * y + (solution1[3] - solution1[1])
                if t > diff:
                    diff = t
                    solutionh = solution1[0]
                    solutionm = solution1[1]
    if len(solution2) > 0:
        if solution2[0] < c or (solution2[0] == c and solution2[1] <= d):
            if solution2[2] > e or (solution2[2] == e and solution2[3] >= f):
                t = (solution2[2] - solution2[0]) * x * y + (solution2[3] - solution2[1])
                if t > diff:
                    diff = t
                    solutionh = solution2[0]
                    solutionm = solution2[1]
    if len(solution4) > 0:
        if solution4[0] < c or (solution4[0] == c and solution4[1] <= d):
            if solution4[2] > e or (solution4[2] == e and solution4[3] >= f):
                t = (solution4[2] - solution4[0]) * x * y + (solution4[3] - solution4[1])
                if t > diff:
                    diff = t
                    solutionh = solution4[0]
                    solutionm = solution4[1]
    if len(solution5) > 0:
        if solution5[0] < c or (solution5[0] == c and solution5[1] <= d):
            if solution5[2] > e or (solution5[2] == e and solution5[3] >= f):
                t = (solution5[2] - solution5[0]) * x * y + (solution5[3] - solution5[1])
                if t > diff:
                    diff = t
                    solutionh = solution5[0]
                    solutionm = solution5[1]
    if len(solution10) > 0:
        if solution10[0] > a or (solution10[0] == a and solution10[1] >= b):
            if solution10[0] < c or (solution10[0] == c and solution10[1] <= d):
                if solution10[2] > e or (solution10[2] == e and solution10[3] >= f):
                    if solution10[2] < g or (solution10[2] == g and solution10[3] <= h):
                        t = (solution10[2] - solution10[0]) * x * y + (solution10[3] - solution10[1])
                        if t > diff:
                            diff = t
                            solutionh = solution10[0]
                            solutionm = solution10[1]
    if len(solution11) > 0:
        if solution11[0] > a or (solution11[0] == a and solution11[1] >= b):
            if solution11[0] < c or (solution11[0] == c and solution11[1] <= d):
                if solution11[2] > e or (solution11[2] == e and solution11[3] >= f):
                    if solution11[2] < g or (solution11[2] == g and solution11[3] <= h):
                        t = (solution11[2] - solution11[0]) * x * y + (solution11[3] - solution11[1])
                        if t > diff:
                            diff = t
                            solutionh = solution11[0]
                            solutionm = solution11[1]
    if len(solution12) > 0:
        if solution12[0] > a or (solution12[0] == a and solution12[1] >= b):
            if solution12[0] < c or (solution12[0] == c and solution12[1] <= d):
                if solution12[2] > e or (solution12[2] == e and solution12[3] >= f):
                    if solution12[2] < g or (solution12[2] == g and solution12[3] <= h):
                        t = (solution12[2] - solution12[0]) * x * y + (solution12[3] - solution12[1])
                        if t > diff:
                            diff = t
                            solutionh = solution12[0]
                            solutionm = solution12[1]
    if len(solution13) > 0:
        if solution13[0] > a or (solution13[0] == a and solution13[1] >= b):
            if solution13[0] < c or (solution13[0] == c and solution13[1] <= d):
                if solution13[2] > e or (solution13[2] == e and solution13[3] >= f):
                    if solution13[2] < g or (solution13[2] == g and solution13[3] <= h):
                        t = (solution13[2] - solution13[0]) * x * y + (solution13[3] - solution13[1])
                        if t > diff:
                            diff = t
                            solutionh = solution13[0]
                            solutionm = solution13[1]
    if len(solution14) > 0:
        if solution14[0] > a or (solution14[0] == a and solution14[1] >= b):
            if solution14[0] < c or (solution14[0] == c and solution14[1] <= d):
                if solution14[2] > e or (solution14[2] == e and solution14[3] >= f):
                    if solution14[2] < g or (solution14[2] == g and solution14[3] <= h):
                        t = (solution14[2] - solution14[0]) * x * y + (solution14[3] - solution14[1])
                        if t > diff:
                            diff = t
                            solutionh = solution14[0]
                            solutionm = solution14[1]

    limit1 = (y - 1 / y) * (f / (x * y)) - e / y
    if limit1 <= a + 1:
        limit1 = a + 1
    limit1 = Decimal(str(int(limit1)))
    limit2 = (y - 1 / y) * (d / (x * y)) - c / y
    if limit2 >= g - 1:
        limit2 = g - 1
    limit2 = Decimal(str(int(limit2)))

    if limit1 >= a + 1 and limit1 <= c - 1:
        solutionNew = solve(limit1, e, 0, x * y, 0, x * y, x, y)
        if len(solutionNew) > 0:
            if solutionNew[0] > a or (solutionNew[0] == a and solutionNew[1] >= b):
                if solutionNew[0] < c or (solutionNew[0] == c and solutionNew[1] <= d):
                    if solutionNew[2] > e or (solutionNew[2] == e and solutionNew[3] >= f):
                        if solutionNew[2] < g or (solutionNew[2] == g and solutionNew[3] <= h):
                            t = (solutionNew[2] - solutionNew[0]) * x * y + (solutionNew[3] - solutionNew[1])
                            if t > diff:
                                diff = t
                                solutionh = solutionNew[0]
                                solutionm = solutionNew[1]
    if limit1 + 1 >= a + 1 and limit1 + 1 <= c - 1:
        solutionNew = solve(limit1 + 1, e, 0, x * y, 0, x * y, x, y)
        if len(solutionNew) > 0:
            if solutionNew[0] > a or (solutionNew[0] == a and solutionNew[1] >= b):
                if solutionNew[0] < c or (solutionNew[0] == c and solutionNew[1] <= d):
                    if solutionNew[2] > e or (solutionNew[2] == e and solutionNew[3] >= f):
                        if solutionNew[2] < g or (solutionNew[2] == g and solutionNew[3] <= h):
                            t = (solutionNew[2] - solutionNew[0]) * x * y + (solutionNew[3] - solutionNew[1])
                            if t > diff:
                                diff = t
                                solutionh = solutionNew[0]
                                solutionm = solutionNew[1]
    if limit2 >= e + 1 and limit2 <= g - 1:
        solutionNew = solve(c, limit2, 0, x * y, 0, x * y, x, y)
        if len(solutionNew) > 0:
            if solutionNew[0] > a or (solutionNew[0] == a and solutionNew[1] >= b):
                if solutionNew[0] < c or (solutionNew[0] == c and solutionNew[1] <= d):
                    if solutionNew[2] > e or (solutionNew[2] == e and solutionNew[3] >= f):
                        if solutionNew[2] < g or (solutionNew[2] == g and solutionNew[3] <= h):
                            t = (solutionNew[2] - solutionNew[0]) * x * y + (solutionNew[3] - solutionNew[1])
                            if t > diff:
                                diff = t
                                solutionh = solutionNew[0]
                                solutionm = solutionNew[1]
    if limit1 - 1 >= e + 1 and limit2 - 1 <= g - 1:
        solutionNew = solve(c, limit2 - 1, 0, x * y, 0, x * y, x, y)
        if len(solutionNew) > 0:
            if solutionNew[0] > a or (solutionNew[0] == a and solutionNew[1] >= b):
                if solutionNew[0] < c or (solutionNew[0] == c and solutionNew[1] <= d):
                    if solutionNew[2] > e or (solutionNew[2] == e and solutionNew[3] >= f):
                        if solutionNew[2] < g or (solutionNew[2] == g and solutionNew[3] <= h):
                            t = (solutionNew[2] - solutionNew[0]) * x * y + (solutionNew[3] - solutionNew[1])
                            if t > diff:
                                diff = t
                                solutionh = solutionNew[0]
                                solutionm = solutionNew[1]

    if solutionh == -1 or diff < 0:
        print("-1")
    else:
        tz = solutionm
        solutionm *= 100
        try:
            r1 = integerPart(solutionm)
            r1 = str(r1)
            r1 = Decimal(r1)
            r2 = solutionm - r1
            if r2 >= Decimal(".5"):
                r1 += Decimal("1")
            t1 = (r1 - r1 % 100) / 100
            t2 = r1 % 100
            t1 = int(t1)
            if t2 == 0:
                t2 = "00"
            elif t2 < 10:
                t2 = "0" + str(t2)
            else:
                t2 = str(t2)
        except:
            exit(0)
        print(str(solutionh) + ":%d.%s" % (t1, t2))
