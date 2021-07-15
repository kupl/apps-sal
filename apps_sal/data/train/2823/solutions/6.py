def duplicates(array):
    return [v for i,v in enumerate(array) if v in array[:i] and array[:i].count(v) == 1]
