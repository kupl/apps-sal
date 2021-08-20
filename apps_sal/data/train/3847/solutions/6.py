def cycle(sequence):
    memo = {}
    for (i, item) in enumerate(sequence):
        if item in memo:
            return [memo[item], i - memo[item]]
        memo[item] = i
    return []
