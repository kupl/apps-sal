from collections import Counter


def sorted_brands(history):
    picked, c = {}, Counter()
    for i, h in enumerate(history):
        c[h['brand']] += 1
        if h['brand'] not in picked:
            picked[h['brand']] = i
    return sorted(c, key=lambda k: (-c[k], picked[k]))
