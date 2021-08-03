import math


def magic(a, digits):
    m = a % 10
    if(m == 4):
        return a + 3
    elif(m == 7):
        p = list(str(a))
        # print p
        for i in range(digits - 1, -1, -1):
            # print p[i]
            if (p[i] == '4'):
                # print 'four'
                p[i] = '7'
                p = ''.join(str(n) for n in p)
                return int(p)
            if ((p[i] == '7') & (i == 0)):
                # print 'seven'
                p[i] = '4'
                p.insert(0, 4)
                p = ''.join(str(n) for n in p)
                return int(p)

            if(p[i] == '7'):
                # print 'seven only'
                p[i] = '4'

            # print p[i]


t = eval(input())

n = []
op = []

for i in range(0, t):
    n.append(eval(input()))

for i in range(0, t):
    digits = int(math.log10(n[i])) + 1
    # print digits
    op.append(magic(n[i], digits))

# for i in range(0,t):
    # print n[i]

for i in range(0, t):
    print(op[i])
