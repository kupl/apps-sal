def regressionLine(x, y):
    sumXSquare = sum([n * n for n in x])
    sumYsquare = sum([n * n for n in y])
    sumXY = sum([X * Y for X, Y in zip(x, y)])
    a = ((sumXSquare * sum(y)) - (sum(x) * sumXY)) / float(((len(x) * sumXSquare) - sum(x) ** 2))
    b = ((len(x) * sumXY) - (sum(x) * sum(y))) / float(((len(x) * sumXSquare) - sum(x) ** 2))
    a = round(a, 4)
    b = round(b, 4)
    return a, b
