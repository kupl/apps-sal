from collections import Counter

def sorted_brands(history):
    brands = [x['brand'] for x in history]
    counter = Counter(brands)
    return sorted(set(brands), key=lambda x: (-counter[x], brands.index(x)))
