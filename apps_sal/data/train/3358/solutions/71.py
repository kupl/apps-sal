def correct(string):
    new_string = string.replace('0', 'O')
    newer_string = new_string.replace('1', 'I')
    newest_string = newer_string.replace('5', 'S')
    return newest_string
