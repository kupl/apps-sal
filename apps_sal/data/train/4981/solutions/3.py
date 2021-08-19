def predict(cnd, p):
    (res, wt) = list(zip(*p))
    return {j: round1(sum((k * l for (k, l) in zip(list(zip(*res))[i], wt))) / sum(wt)) for (i, j) in enumerate(cnd)}
