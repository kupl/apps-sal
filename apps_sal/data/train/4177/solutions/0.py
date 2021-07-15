def men_from_boys(arr):
    men = []
    boys = []
    for i in sorted(set(arr)):
        if i % 2 == 0:
            men.append(i)
        else:
            boys.append(i)
    return men + boys[::-1]
