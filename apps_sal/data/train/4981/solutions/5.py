def predict(candidates, polls):
    total_weight = sum(w for p, w in polls)
    return {
        c: round1(sum(ps[i] * w for ps, w in polls) / total_weight)
        for i, c in enumerate(candidates)
    }
