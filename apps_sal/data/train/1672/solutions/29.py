l = [0 for i in range(11)]
for i in range(11):
    l[i] = int(input())
l.reverse()
for i in l:
    a = i ** 3 * 5 + abs(i) ** 0.5
    if a > 400:
        print('f(' + str(i) + ') = MAGNA NIMIS!')
        continue
    print('f(' + str(i) + ') =', format(a, '.2f'))
