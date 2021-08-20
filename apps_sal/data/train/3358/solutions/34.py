def correct(string):
    output = ''
    for i in range(len(string)):
        if string[i] == '5':
            output = output + 'S'
        elif string[i] == '0':
            output = output + 'O'
        elif string[i] == '1':
            output = output + 'I'
        else:
            output = output + string[i]
    return output
