CA = []
IA = []
for II_II in range(eval(input())):
    n = eval(input())
    for KK_KK in range(n):
        (cof, exp) = list(map(int, input().split()))
        if exp == 0:
            continue
        if exp > 1:
            CA.append(str(cof * exp) + 'x^' + str(exp - 1))
        if exp == 1:
            IA.append(cof * exp)
    k = sum(IA)
    if k > 0:
        CA.append(str(k))
    str1 = ' + '.join((str(e) for e in CA))
    if len(str1) >= 1:
        print(str1)
    else:
        print('0')
    CA[:] = []
    IA[:] = []
