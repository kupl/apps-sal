def cycle(sequence):
    found = {}
    for i, item in enumerate(sequence):
        if item in found:
            return [found[item], i - found[item]]
        found[item] = i
    else:
        return []
