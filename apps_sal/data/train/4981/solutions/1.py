def predict(candidates, polls):
    weight = sum((w for (_, w) in polls))
    scores = zip(*([s * w for s in r] for (r, w) in polls))
    return dict(zip(candidates, (round1(sum(s) / weight) for s in scores)))
