def men_from_boys(arr):
    men = [x for x in arr if x % 2 == 0]
    boys = [x for  x in arr if x % 2 != 0]
    return sorted(set(men)) + sorted(set(boys), reverse = True)
