def men_from_boys(arr):
    chad = sorted([x for x in list(dict.fromkeys(arr)) if x % 2 == 0])
    virgin = sorted([x for x in list(dict.fromkeys(arr)) if x % 2 == 1], reverse=True)
    return chad + virgin
