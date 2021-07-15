def order_weight(strng):
    nums = sorted(strng.split())
    weights = [sum(map(int, n)) for n in nums]
    res = [n for w, n in sorted(zip(weights, nums))]
    return ' '.join(res)
