def numericals(s):
    seen_liters = {l: 0 for l in set(s)}
    result = ''
    for l in s:
        seen_liters[l] += 1
        result += str(seen_liters[l])
    return result
