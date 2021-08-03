def switcheroo(string):
    return string.translate(string.maketrans('ab', 'ba'))
