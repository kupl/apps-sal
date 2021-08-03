def predict(candidates, polls):
    res = dict()
    for i in range(len(candidates)):
        p = 0
        s = 0
        for poll in polls:
            p += poll[0][i] * poll[1]
            s += poll[1]
        res[candidates[i]] = round1(p / s)
    return res
