def solve(arr):
    x = []
    for element in arr:
        if element in x:
            x.remove(element)
            x.append(element)
        else:
            x.append(element)
    return x
