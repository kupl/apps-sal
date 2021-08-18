def dashatize(num):
    array = []

    if num == None:
        return "None"
    elif num == 0:
        return "0"
    elif num == -1:
        return "1"

    num = str(num).replace('-', '')

    for i in str(num):
        if int(i) % 2 == 0:
            array.append(i)
        else:
            array.append('-' + i + '-')

    string = ''.join(array)

    if string[0] == '-' and string[-1] == '-':
        string = string[1:-1]
    if string[0] == '-':
        string = string[1:]
    if string[-1] == '-':
        string = string[:-1]
    result = string.replace('--', '-')

    return result
