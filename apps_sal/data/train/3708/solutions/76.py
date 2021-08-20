def hex_to_dec(s):
    letter_conversions = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    result = 0
    for (index, digit) in enumerate(s[::-1]):
        if digit.isnumeric():
            result += int(digit) * 16 ** index
        else:
            for (key, value) in letter_conversions.items():
                if digit == key:
                    result += value * 16 ** index
    return result
