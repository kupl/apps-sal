def men_from_boys(arr):
    men = sorted(set([x for x in arr if x % 2 == 0]))
    boys = sorted(set([x for x in arr if x % 2 == 1]), reverse=True)
    return men + boys
