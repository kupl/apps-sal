# KenKamau's solution
def max_match(st):
    for i in range(len(st), 0, -1):
        if i == 1 or st[:i] in VALID_WORDS:
            return [st[:i]] + max_match(st[i:])
    return []
