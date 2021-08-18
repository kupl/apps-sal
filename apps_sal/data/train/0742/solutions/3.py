def SR(coeff):
    size = len(coeff)
    max_power = size - 1
    Arr = []
    row1 = coeff[0::2]
    row2 = coeff[1::2]
    ln = len(row1)
    if size % 2 != 0:
        row2.append(0)
    row1.append(0)
    row2.append(0)
    Arr.append(row1)
    Arr.append(row2)

    def sign(x): return 1 if x > 0 else -1
    s = [sign(row1[0]), sign(row2[0])]

    for r in range(2, size):
        Arr.append([0] * (ln + 1))

        for n in range(ln):
            Arr[r][n] = (Arr[r - 1][0] * Arr[r - 2][n + 1]) - (Arr[r - 2][0] * Arr[r - 1][n + 1])

        s.append(sign(Arr[r][0]))

    ''' If all the element of that row is zero case
    then nth element = nth element of its previous row *
    ((max. power of x) - 4 - r - 2n ) '''
    for i in range(len(Arr)):
        if list(set(Arr[i])) == [0]:
            for n in range(len(Arr[i])):
                Arr[i][n] = (Arr[i - 1][n] * (max_power + 4 - (i + 1) - (2 * (n + 1))))

        elif Arr[i][0] == 0:
            return 0

    ''' check if sign change '''
    if len(set(s)) == 1:
        return 1
    else:
        return 0


T = int(input())
for t in range(T):
    coeff = [int(x) for x in input().split()]
    print(SR(coeff))
