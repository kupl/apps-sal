def stringy(size):
    # Good Luck!
    value = True
    result = ''
    for i in range(size):
        result += str(int(value))
        value = not value
    return result
