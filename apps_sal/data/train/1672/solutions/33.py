num = []
for i in range(11):
    num.append(int(input()))
num = num[::-1]

for x in num:
    val = (x ** 3) * 5 + abs(x) ** 0.5

    if val > 400:
        print('f({}) = MAGNA NIMIS!'.format(x))
    else:
        print('f({}) = {:.2f}'.format(x, val))
