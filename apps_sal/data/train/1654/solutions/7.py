import operator


def solve_runes(runes):
    r = [x for x in runes]
    print(runes)
    a = []
    b = []
    c = []
    d = ['+', '-', '*', '=']
    s = []
    cntr = 0
    scntr = 0
    for i in r:
        if r.index(i) == 0 and r[0] == '-' and (scntr == 0):
            a.append(i)
            scntr += 1
        elif r.index(i) != 0 and i not in d:
            a.append(i)
        elif r.index(i) == 0 and i not in d:
            a.append(i)
        elif r.index(i) != 0 and i in d:
            s.append(i)
            break
        elif i in d and scntr != 0 and (i == '-'):
            s.append(i)
            break
        cntr += 1
    cntr2 = 0
    r1 = r[cntr + 1:]
    for i in r1:
        if r1.index(i) == 0 and r1[0] == '-':
            b.append(i)
        elif r1.index(i) != 0 and i not in d:
            b.append(i)
        elif r1.index(i) == 0 and i not in d:
            b.append(i)
        elif r1.index(i) != 0 and i in d:
            break
        cntr2 += 1
    r2 = r[cntr + cntr2 + 2:]
    for i in r2:
        if r2.index(i) == 0 and r2[0] == '-':
            c.append(i)
        elif r2.index(i) != 0 and i not in d:
            c.append(i)
        elif r2.index(i) == 0 and i not in d:
            c.append(i)
        elif r2.index(i) != 0 and i in d:
            break
    number = list(range(0, 10))
    number2 = list(range(1, 10))
    op = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    alist = [a, b, c]
    ilist = []
    for i in alist:
        for x in i:
            if x == '-' and i.index(x) == 0:
                if i[1] == '?':
                    ilist.append('nZero')
                    break
            elif x == '?' and i.index(x) == 0 and (len(i) != 1):
                ilist.append('nZero')
                break
            else:
                ilist.append('yZero')
                break
    num = []
    num2 = []
    print((a, b, c))
    for i in number:
        if str(i) not in a and str(i) not in b and (str(i) not in c):
            num.append(i)
    for i in number2:
        if str(i) not in a and str(i) not in b and (str(i) not in c):
            num2.append(i)
    if 'nZero' in ilist:
        for n in num2:
            a1 = [str(n) if x == '?' else x for x in a]
            b1 = [str(n) if x == '?' else x for x in b]
            c1 = [str(n) if x == '?' else x for x in c]
            a1 = int(''.join(a1))
            b1 = int(''.join(b1))
            c1 = int(''.join(c1))
            if op[s[0]](a1, b1) == c1:
                return n
    if 'nZero' not in ilist:
        for n in num:
            a1 = [str(n) if x == '?' else x for x in a]
            b1 = [str(n) if x == '?' else x for x in b]
            c1 = [str(n) if x == '?' else x for x in c]
            a1 = int(''.join(a1))
            b1 = int(''.join(b1))
            c1 = int(''.join(c1))
            if op[s[0]](a1, b1) == c1:
                return n
    return -1
