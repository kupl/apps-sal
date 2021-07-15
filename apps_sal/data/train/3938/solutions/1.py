def sorted_brands(history):
    brands = [item['brand'] for item in history]
    return sorted(set(brands), key=lambda x: (-brands.count(x), brands.index(x)))
