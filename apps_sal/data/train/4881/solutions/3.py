def camelize(str_):
    new_str = ''
    new_word = True
    for elem in str_:
        if elem.isalnum():
            new_str += elem.upper() if new_word else elem.lower()
            new_word = False
        else:
            new_word = True
    return new_str
