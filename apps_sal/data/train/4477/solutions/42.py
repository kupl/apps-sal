def reverse_number(n):

    if n >= 0:

        d = [int(i) for i in str(n)]

        r = d[::-1]

        w = int(''.join(map(str, r)))

        return w

    if n < 0:

        m = abs(n)

        d = [int(j) for j in str(m)]

        r = d[::-1]

        w = int(''.join(map(str, r)))

        return w * -1
