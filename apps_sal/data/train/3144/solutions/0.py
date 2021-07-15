from collections import Counter

def number_of_pairs(gloves):
    return sum(c // 2 for c in Counter(gloves).values())
