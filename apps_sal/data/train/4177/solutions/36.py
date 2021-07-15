def men_from_boys(arr):
    mens = sorted([x for x in set(arr) if x % 2 == 0])
    boys = sorted([x for x in set(arr) if x % 2 == 1], reverse=True)
    return list(mens + boys)
