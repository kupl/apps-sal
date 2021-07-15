def gimme(array):
    first = array[0]
    second = array[1]
    third = array[2]
    if first <= second <= third:
        return 1
    elif first <= third <= second:
        return 2
    elif second <= first <= third:
        return 0
    elif second <= third <= first:
        return 2
    elif third <= first <= second:
        return 0
    elif third <= second <= first:
        return 1

