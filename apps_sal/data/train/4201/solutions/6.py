def find_missing(se):
    step = (se[-1] - se[0]) / len(se)
    ls = [se[0] + i * step for i in range(0, len(se) + 1)]
    return sum(ls) - sum(se)
