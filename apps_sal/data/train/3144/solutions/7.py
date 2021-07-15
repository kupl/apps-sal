def number_of_pairs(gloves):
    return sum([gloves.count(i) // 2 for i in set(gloves)])
