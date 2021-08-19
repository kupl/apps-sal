def toFixed(numObj, digits=0):
    return f'{numObj:.{digits}f}'


rome = [None] * 11
for nextum in range(11):
    rome[-nextum - 1] = int(input())
for nextum in rome:
    resultum = (nextum ** 2) ** 0.25 + 5 * nextum ** 3
    if resultum <= 400:
        print('f({}) = {:.2f}'.format(nextum, resultum))
    else:
        print('f({}) = MAGNA NIMIS!'.format(nextum))
