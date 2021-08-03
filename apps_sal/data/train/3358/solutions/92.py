def correct(string):
    correct = {'5': 'S', '0': 'O', '1': 'I'}
    for i in correct:
        string = string.replace(i, correct[i])
    return string
