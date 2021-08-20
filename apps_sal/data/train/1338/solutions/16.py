l = [i for i in input().split()]
i = 1
n = len(l)
while i <= n - 1:
    print('%.2f' % round(float(l[i]) * pow(10, int(l[i + 1])), 2))
    i += 2
