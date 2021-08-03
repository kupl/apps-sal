def correct(string):
    correct = ''
    for i in string:
        if i == '5':
            correct += 'S'
        elif i == '0':
            correct += 'O'
        elif i == '1':
            correct += 'I'
        else:
            correct += i

    return correct
