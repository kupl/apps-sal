def men_from_boys(arr):
    (men, boys) = ([], [])
    for v in set(arr):
        if v % 2 == 0:
            men.append(v)
        else:
            boys.append(v)
    return sorted(men) + sorted(boys, reverse=True)
