def men_from_boys(arr):
    a = sorted([x for x in list(set(arr)) if x % 2 == 0])
    b = sorted([x for x in list(set(arr)) if x % 2 != 0], reverse=True)
    return a + b
