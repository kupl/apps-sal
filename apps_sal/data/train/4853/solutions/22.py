def addition(char):
    return 2 * char


def double_char(s):
    result = list(map(addition, s))
    return ''.join(result)
