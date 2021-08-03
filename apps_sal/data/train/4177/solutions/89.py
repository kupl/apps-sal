def men_from_boys(arr):
    men = []
    boys = []
    for i in arr:
        if i % 2 == 0 and i not in men:
            men.append(i)
        if i % 2 != 0 and i not in boys:
            boys.append(i)
    men.sort()
    boys.sort()
    boys.reverse()
    return men + boys
