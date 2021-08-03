def is_palindrome(string):
    if type(string) == int:
        line = str(string)
    else:
        line = string
    n = len(line) - 1
    chars = []

    while (n >= 0):
        char = line[n]
        chars.append(char)
        n -= 1

    new_string = ''.join(chars)
    return line == new_string
