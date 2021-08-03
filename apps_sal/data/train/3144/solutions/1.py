def number_of_pairs(gloves):
    return sum(gloves.count(color) // 2 for color in set(gloves))
