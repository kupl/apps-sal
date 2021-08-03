def crashing_weights(weights):
    if len(weights) < 2:
        return weights[0]
    result = []
    for row in zip(*weights):
        cur = row[0]
        for nxt in row[1:]:
            cur = cur + nxt if cur > nxt else nxt
        result.append(cur)
    return result
