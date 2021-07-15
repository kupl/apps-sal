def men_from_boys(arr):
    boys = []
    men = []
    for elem in set(arr):
        if elem % 2:
            boys.append(elem)
        else:
            men.append(elem)
    return sorted(men) + sorted(boys, reverse=True)
