def min_and_max(l, d, x):
    listOfCorect = [num for num in list(range(l, d + 1)) if sum(map(int, str(num))) == x]
    return [min(listOfCorect), max(listOfCorect)]
