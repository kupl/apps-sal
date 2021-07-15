def correct(string):
    dict = {'0': 'O', '1': 'I', '5': 'S'}
    output = ''
    for x in string:
        if x.isdigit():
            output += dict[x]
        else:
            output += x
    return output
