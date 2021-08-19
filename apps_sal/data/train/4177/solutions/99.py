def men_from_boys(arr):
    men = set([h for h in arr if h % 2 == 0])
    boys = set(arr) - set(men)
    return sorted(men) + sorted(boys, reverse=True)
