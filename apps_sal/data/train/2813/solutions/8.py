def switcher(arr):
    return ''.join((chr(123 - int(i)) for i in arr)).translate(str.maketrans('`_^', '!? '))
