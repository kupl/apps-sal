def regressionLine(x, y):

    def sq(p):
        return sum([i * i for i in p])
    xy = sum(map(lambda p, q: p * q, x, y))
    return (round((sq(x) * sum(y) - sum(x) * xy) / (len(x) * sq(x) - sum(x) * sum(x)), 4), round((len(x) * xy - sum(x) * sum(y)) / (len(x) * sq(x) - sum(x) * sum(x)), 4))
