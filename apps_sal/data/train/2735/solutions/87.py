def jumping_number(number):
    arr = list(map(int, str(number)))
    return ['Not!!', 'Jumping!!'][all(map(lambda x, y: abs(x - y) == 1, arr, arr[1:]))]
