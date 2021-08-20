def min_value(digits):
    empty = []
    string = ''
    for i in digits:
        if i not in empty:
            empty.append(i)
    empty.sort()
    for x in empty:
        string += str(x)
    return int(string)
