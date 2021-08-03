def get_pins(observed):

    numbers = {
        '1': [1, 4, 2],
        '2': [1, 2, 3, 5],
        '3': [2, 3, 6],
        '4': [1, 4, 5, 7],
        '5': [2, 4, 5, 6, 8],
        '6': [3, 5, 6, 9],
        '7': [4, 7, 8],
        '8': [0, 5, 7, 8, 9],
        '9': [6, 8, 9],
        '0': [0, 8]
    }

    from itertools import product
    possible = [numbers[o] for o in observed]
    return [''.join(map(str, p)) for p in product(*possible)]
