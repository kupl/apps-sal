def find_longest(arr):
    return arr[[len(str(element)) for element in arr].index(max([len(str(element)) for element in arr]))]
