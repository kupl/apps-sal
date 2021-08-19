def men_from_boys(arr):
    sorted_unique_arr = sorted(set(arr))
    (men, boys) = ([], [])
    for d in sorted_unique_arr:
        if d % 2 == 0:
            men = men + [d]
        else:
            boys = [d] + boys
    return men + boys
