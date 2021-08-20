def next(a, b):
    return 3 - (a + b) % 3


def rgb_to_number(string):
    rgb = ['R', 'G', 'B']
    return [rgb.index(x) + 1 for x in string]


def triangle(row):
    number_dict = {1: 'R', 2: 'G', 3: 'B'}
    row = rgb_to_number(row)
    while len(row) > 1:
        row = [next(row[i], row[i + 1]) for i in range(len(row) - 1)]
    return number_dict[row[0]]
