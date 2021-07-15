def get_derivative(string):
    if string.endswith('x'):
        return string.split('x')[0]
    elif len(string) == 1:
        return '0'
    else:
        s = list(map(int, string.split("x^")))
        second = s[1] - 1
        return f"{s[0] * s[1]}x{'^' + str(second) if second != 1 else ''}"
