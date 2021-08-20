from collections import Counter


def sorted_brands(history):
    cnt = Counter((item['brand'] for item in history))
    return sorted(cnt, key=cnt.get, reverse=True)
