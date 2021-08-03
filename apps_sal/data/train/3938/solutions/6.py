from collections import Counter


def sorted_brands(history):
    return [n[0] for n in Counter([n['brand'] for n in history]).most_common()]
