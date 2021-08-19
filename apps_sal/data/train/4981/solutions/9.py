def predict(candidates, polls):
    wts = [i[1] for i in polls]
    return dict(zip(candidates, map(lambda z: round1(sum((a * b for (a, b) in zip(z, wts))) / sum(wts)), zip(*(i[0] for i in polls)))))
