def correct(string):
    for i in string:
        if i == '0':
            string = string.replace('0', 'O')
            print(string)
        elif i == '1':
            string = string.replace('1', 'I')
        elif i == '5':
            string = string.replace('5', 'S')
    return string
