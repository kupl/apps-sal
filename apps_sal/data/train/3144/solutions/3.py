from collections import Counter

def number_of_pairs(gloves):
    return sum(num // 2 for num in Counter(gloves).values())
