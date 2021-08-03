from collections import defaultdict


def numericals(stg):
    count, result = defaultdict(int), []
    for c in stg:
        count[c] += 1
        result.append(f"{count[c]}")
    return "".join(result)
