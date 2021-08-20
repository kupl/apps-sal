def string_to_number(s):
    result = 0
    place = 1
    i = len(s) - 1
    while i >= 0:
        digit = s[i]
        if digit == '1':
            result += place
        elif digit == '2':
            result += 2 * place
        elif digit == '3':
            result += 3 * place
        elif digit == '4':
            result += 4 * place
        elif digit == '5':
            result += 5 * place
        elif digit == '6':
            result += 6 * place
        elif digit == '7':
            result += 7 * place
        elif digit == '8':
            result += 8 * place
        elif digit == '9':
            result += 9 * place
        elif digit == '-':
            result = -result
        place *= 10
        i -= 1
    return result
