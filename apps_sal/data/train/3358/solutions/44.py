def correct(string):
    wrong = ['5', '0', '1']
    right = ['S', 'O', 'I']
    for x in wrong:
        string = string.replace(x, right[wrong.index(x)])
    return string
