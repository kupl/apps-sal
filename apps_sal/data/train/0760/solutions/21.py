import math
MAX = ((10**9) + 7)
t = int(input())
while t > 0:
    x = input()
    d = {}
    count = 0
    l = len(x)
    for item in range(l):
        flag = 0
        for i in d:
            if i == x[item]:
                flag = 1
                d[i] += 1
                break
        if flag == 0:
            d.fromkeys(x[item])
            d[x[item]] = 1
    y = []
    for item in d:
        y.append(d[item])
    prod = 1
    q = len(y)
    for item in range(q):
        prod *= math.factorial(y[item])
        if y[item] > 1:
            count += 1

    def bruce():
        Sum2 = 0
        Sum3 = 0
        Sum4 = 0
        Sum5 = 0
        Sum6 = 0
        for i in range(q):
            temp3 = 0
            if y[i] > 1:
                temp3 = y[i] * ((y[i] - 1) / 2)
            for j in range(i + 1, q):
                temp1 = 0
                temp2 = 0
                Sum2 += y[i] * y[j]
                if y[i] > 1:
                    temp1 = y[i] * (y[i] - 1) / 2
                if y[j] > 1:
                    temp2 = y[j] * (y[j] - 1) / 2
                Sum5 += temp1 * temp2
                for k in range(j + 1, q):
                    Sum3 += y[i] * y[j] * y[k]
                    # print y[i],y[j],y[k]
                    if y[i] > 1:
                        Sum6 += (y[i] * (y[i] - 1)) / 2 * y[j] * y[k]
                        # print Sum6
                    if y[j] > 1:
                        Sum6 += y[i] * (y[j] * (y[j] - 1)) / 2 * y[k]
                    # print Sum6
                    if y[k] > 1:
                        Sum6 += y[i] * y[j] * (y[k] * (y[k] - 1)) / 2
                    # print Sum6
                    for z in range(k + 1, q):
                        Sum4 += y[i] * y[j] * y[k] * y[z]
        # print "Sum2=%d,Sum3=%d,Sum4=%d,Sum5=%d,Sum6=%d"%(Sum2,Sum3,Sum4,Sum5,Sum6)
        return ((Sum2 % MAX + (Sum3 * 2) % MAX + (Sum4 * 3) % MAX + Sum5 % MAX + (Sum6 * 2) % MAX))
    ans1 = bruce()
    fact = math.factorial(l)
    # print "fact=%d,prod=%d"%(fact,prod)
    ast = fact / prod
    # print ast
    temp = (((ast) % MAX) * ((ast - 1) % MAX)) % MAX
    RRR = ((ast % MAX) * (ans1 % MAX)) % MAX
    ans = (temp - RRR + MAX) % MAX
    print(ans)
    t -= 1
