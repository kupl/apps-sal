def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]
