def men_from_boys(a):
    return sorted({x for x in a if x % 2 == 0}) + sorted({x for x in a if x % 2 != 0}, reverse=True)
