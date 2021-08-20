from itertools import product
PINS = {'1': '124', '2': '1253', '3': '236', '4': '1457', '5': '24568', '6': '3569', '7': '478', '8': '57890', '9': '689', '0': '08'}


def get_pins(observed):
    return list(map(''.join, product(*[PINS[num] for num in observed])))
