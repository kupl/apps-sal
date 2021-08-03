from re import findall


def square_it(digits):
    digits_string = str(digits)
    root = len(digits_string) ** 0.5
    if root.is_integer():
        return '\n'.join(findall('.{' + str(int(root)) + '}', digits_string))
    return 'Not a perfect square!'
