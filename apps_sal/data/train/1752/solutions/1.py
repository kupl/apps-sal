def get_pins(observed):
    map = [['8', '0'], ['1', '2', '4'], ['1', '2', '3', '5'], ['2', '3', '6'], ['1', '4', '5', '7'], ['2', '4', '5', '6', '8'],
           ['3', '5', '6', '9'], ['4', '7', '8'], ['5', '7', '8', '9', '0'], ['6', '8', '9']]
    return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]
