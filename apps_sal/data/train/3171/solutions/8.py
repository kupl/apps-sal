def crashing_weights(weights):
    r = []
    for t in zip(*weights):
        l = list(t)
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                l[i] += l[i - 1]
        r.append(l[-1])
    return r
