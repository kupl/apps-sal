a = list(map(float, input().split()))
for i in range(int(a[0])):
    print('%0.2f' % (a[2 * i + 1] * 10 ** a[2 * i + 2]))
