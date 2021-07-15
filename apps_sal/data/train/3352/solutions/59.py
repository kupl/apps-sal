def find_longest(arr):
    length = 0
    noomber = 0
    for x in arr:
        if length < len(str(x)):
            noomber = x
            length = len(str(x))
    return noomber
