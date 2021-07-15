def solve(stg):
    split = [[], []]
    for c in sorted(stg):
        split[0 if c in "aeiou" else 1].append(c)
    a, b = sorted(split, key=len, reverse=True)
    if len(a) - len(b) > 1:
        return "failed"
    result = [""] * len(stg)
    result[::2], result[1::2] = a, b
    return "".join(result)
