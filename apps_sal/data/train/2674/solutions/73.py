def two_sort(array):
    first_item = sorted([i for i in array])[0]
    formatted = ""
    for i in first_item:
        formatted = formatted + i +"***"
    return formatted[:-3]

