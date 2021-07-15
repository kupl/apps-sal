def correct(string):
    errors = {'5' : 'S',
              '0' : 'O',
              '1' : 'I'}
    n_str = ""
    for letter in string:
        if letter in errors:
            letter = errors[letter]
        n_str = n_str + letter   
    return n_str
