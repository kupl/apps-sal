from collections import Counter


def most_frequent_item_count(collection):
    return max(Counter(collection).values(), default=0)
