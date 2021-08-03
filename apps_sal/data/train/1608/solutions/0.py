def determinant(m):
    a = 0
    if len(m) == 1:
        a = m[0][0]
    else:
        for n in xrange(len(m)):
            if (n + 1) % 2 == 0:
                a -= m[0][n] * determinant([o[:n] + o[n + 1:] for o in m[1:]])
            else:
                a += m[0][n] * determinant([o[:n] + o[n + 1:] for o in m[1:]])

    return a
