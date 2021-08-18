lip = ['0.00', '6.00', '-3642.00', '-2557.17', '-1712.35', '-1077.55', '-622.76', '-318.00', '-133.27', '-38.59', 'MAGNA NIMIS!']
s = []
for i in range(11):
    s.append(int(input()))
s.reverse()
for i in range(0, 11):
    a = s[i]**3 * 5
    b = abs(s[i])**0.5
    ans = a + b
    print('f(' + str(s[i]) + ") = ", end='')

    if (ans < 400):
        print('{:.2f}'.format(ans))
    else:
        print(' MAGNA NIMIS!')
