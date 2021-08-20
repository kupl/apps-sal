def men_from_boys(arr):
    distinct = set(arr)
    men = sorted((m for m in distinct if m % 2 == 0))
    boys = sorted((b for b in distinct if b % 2), reverse=True)
    return men + boys
