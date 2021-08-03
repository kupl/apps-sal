def find_longest(arr):
    b = 0
    result = 0
    for i in arr:
        if len(str(i)) > b:
            b = len(str(i))
            result = i
    return (result)
