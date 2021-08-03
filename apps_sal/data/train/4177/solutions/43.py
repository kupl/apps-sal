def men_from_boys(arr):
    arr = list(set(arr))
    men = [i for i in arr if i % 2 == 0]
    boys = [i for i in arr if i % 2 == 1]
    men = sorted(men)
    boys = sorted(boys, reverse=True)
    return men + boys
