def stringy(size):
    (start, result) = ('1', '')
    for i in range(size):
        result += start
        start = '1' if start == '0' else '0'
    return result
