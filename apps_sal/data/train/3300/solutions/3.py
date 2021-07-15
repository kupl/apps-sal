TR = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa')

def replace_letters(word):
    return word.translate(TR)
