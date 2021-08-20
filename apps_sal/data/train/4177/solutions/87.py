def men_from_boys(arr):
    men = sorted(list(dict.fromkeys([x for x in arr if x % 2 == 0])))
    boys = sorted(list(dict.fromkeys([x for x in arr if x % 2 != 0])), reverse=True)
    return men + boys
