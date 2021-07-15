def number_of_pairs(gloves):
    return sum(gloves.count(c) // 2 for c in set(gloves))
