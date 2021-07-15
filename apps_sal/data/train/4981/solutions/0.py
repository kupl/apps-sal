def predict(candidates, polls):
    x = zip(*[list(map(lambda i: i * weight, poll)) for poll, weight in polls])
    x = list(map(round1, (map(lambda i: sum(i) / sum([i[1] for i in polls]), x))))
    return dict(zip(candidates,x))
