def outcome(n, s, k):
    from itertools import zip_longest
    dice = [1]
    for _ in range(n):
        dice = [sum(x) for x in zip_longest(*([0] * i + dice for i in range(1, s + 1)), fillvalue=0)]
    return dice[k] if k < len(dice) else 0
