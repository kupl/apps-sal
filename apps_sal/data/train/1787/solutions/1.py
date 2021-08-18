def row(m, r): return m[r]
def col(m, c): return [r[c] for r in m]


def row_mul(m, r, coeff): return [[v * coeff for v in row] if rr == r else row for rr, row in enumerate(m)]
def row_add(m, r1, r2, coeff=1): return [[v1 + v2 * coeff for v1, v2 in zip(row, m[r2])] if rr == r1 else row for rr, row in enumerate(m)]


class Datamining:

    def __init__(self, train_set):
        """
        Given the training set build a set of polynomial regression coefficients
        Up to a maximum of degree 10.
        Yay for linear algebra!
        """
        N = len(train_set)
        P = N - 1
        P = min(10, P)
        xs, ys = [t[0] for t in train_set], [t[1] for t in train_set]

        m = [[sum(xs[i] ** (p1 + p2) for i in range(N)) for p2 in range(P)] for p1 in range(P)]
        r = [sum(ys[i] * xs[i] ** p for i in range(N)) for p in range(P)]
        m = [m[i] + [r[i]] for i in range(P)]

        for r in range(P):
            if m[r][r] == 0:
                vs = col(m, r)
                for rr, v in enumerate(vs):
                    if rr > r and v != 0:
                        break
                m = row_add(m, r, rr, 1 / m[rr][r])
            else:
                m = row_mul(m, r, 1 / m[r][r])

            for cr in range(P):
                if cr != r:
                    f = m[cr][r]
                    if f != 0:
                        m = row_add(m, cr, r, -f)

        self.coeffs = col(m, -1)
        print(("coeffs: {}".format([round(c, 4) for c in self.coeffs])))

    def predict(self, x):
        """Use calculated coefficients to predict next y given x"""
        return sum(c * (x ** p) for p, c in enumerate(self.coeffs))
