def tv_remote(word):
    keyboard = [
        ["a", "b", "c", "d", "e", "1", "2", "3"],
        ["f", "g", "h", "i", "j", "4", "5", "6"],
        ["k", "l", "m", "n", "o", "7", "8", "9"],
        ["p", "q", "r", "s", "t", ".", "@", "0"],
        ["u", "v", "w", "x", "y", "z", "_", "/"]
    ]
    result = 0
    coordinates1 = [0, 0]

    for letter in word:
        coordinates2 = find_symbol_coordinates(letter, keyboard)
        result += abs(coordinates2[1] - coordinates1[1]) + abs(coordinates2[0] - coordinates1[0]) + 1
        coordinates1 = find_symbol_coordinates(letter, keyboard)
    return result


def find_symbol_coordinates(symbol, array):
    x = 0
    y = 0
    for row in array:
        for colomn in row:
            if colomn == symbol:
                return [x, y]
            x += 1
        y += 1
        x = 0
