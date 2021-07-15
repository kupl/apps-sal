def men_from_boys(arr):
    return sorted(list(set(x for x in arr if x%2 ==0))) + sorted(list(set(y for y in arr if y%2 != 0)),reverse = True)
