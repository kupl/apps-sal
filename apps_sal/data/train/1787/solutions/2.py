def reduced_echelon_form(matrix):
    matrix = matrix[::]
    if not matrix:
        return
    lead = 0
    row_count = len(matrix)
    column_count = len(matrix[0])
    for r in range(row_count):
        if lead >= column_count:
            return matrix
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if column_count == lead:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [mrx / float(lv) for mrx in matrix[r]]
        for i in range(row_count):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [iv - lv * rv for rv, iv in zip(matrix[r], matrix[i])]
        lead += 1

    return matrix


class Poly:
    def __init__(self, k, coef, lambda_=[1]):
        vector = [(_[1], e)for e, _ in enumerate(zip(range(0, k + 1), coef))]
        self.poly = vector
        self.lambda_ = lambda_

    def eval_poly(self, x):
        return sum(l * pe[0] * x**pe[1] for pe, l in zip(self.poly, self.lambda_))

    def _to_string(self):
        s = ""
        for p, e in self.poly[::-1]:
            s += "{}{}x^{}" . format("+" if p >= 0 else "", p, e)
        s = s.strip("+")
        return s


class Datamining:

    def __init__(self, train_set):
        self.train = train_set
        self.copy = train_set[::]
        self._learn()

    def _mse(self, corr, pred):
        s = [(c - p) ** 2 for c, p in zip(corr, pred)]
        return sum(s) / len(s)

    def frange(self, start, end, step):
        while start < end:
            yield start
            start += step

    def _learn(self):
        from random import shuffle
        train_perc = 0.65
        iterations = 18
        best = set()
        deg = 0
        lmbds = self.frange(0.7, 1.3, 0.1)
        degrees = range(2, 6)
        for l in lmbds:
            for d in degrees:
                for iter in range(iterations):
                    m = []
                    tmp = []
                    for p in self.train[:deg + 1 + d]:
                        x = p[0]
                        y = p[1]
                        tmp = [x**e for e in range(deg + 1 + d)]
                        tmp.append(y)
                        m.append(tmp)

                    mtx = reduced_echelon_form(m)
                    coef = [r[-1] for r in mtx]

                    shuffle(self.copy)

                    ntrain = int(len(self.copy) * train_perc)
                    train = self.copy[:ntrain]
                    test = self.copy[ntrain:]

                    poly = Poly(deg + d, coef, lambda_=[l for _ in range(deg + d)])
                    model = poly.eval_poly

                    predicted = [model(p[0]) for p in test]
                    correct = [p[1] for p in test]

                    best.add((self._mse(predicted, correct), poly))

        _, poly = min(best, key=lambda x: x[0])
        self.model = poly.eval_poly

    def predict(self, x):
        return self.model(x)
