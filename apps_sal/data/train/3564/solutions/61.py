def stringy(size):
    string = []
    for i in range(size):
        if i % 2 == 1:
            string.append('0')
        else:
            string.append('1')
    return ''.join(string)
