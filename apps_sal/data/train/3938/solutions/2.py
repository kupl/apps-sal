from collections import Counter


def sorted_brands(history):
    brands = Counter((x['brand'] for x in history))
    return [brand for (brand, _) in brands.most_common()]
