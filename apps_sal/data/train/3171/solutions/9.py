def crashing_weights(weights):
    result = []
    for row in zip(*weights):
        if len(row) < 2:
            return weights[0]
        cur = row[0]
        for nxt in row[1:]:
            cur = cur + nxt if cur > nxt else nxt
        result.append(cur)
    return result
