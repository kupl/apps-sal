adjacents = {
    '1': ['2', '4'],
    '2': ['1', '5', '3'],
    '3': ['2', '6'],
    '4': ['1', '5', '7'],
    '5': ['2', '4', '6', '8'],
    '6': ['3', '5', '9'],
    '7': ['4', '8'],
    '8': ['5', '7', '9', '0'],
    '9': ['6', '8'],
    '0': ['8'],
}


def get_pins(observed):
    if len(observed) == 1:
        return adjacents[observed] + [observed]
    return [a + b for a in adjacents[observed[0]] + [observed[0]] for b in get_pins(observed[1:])]
