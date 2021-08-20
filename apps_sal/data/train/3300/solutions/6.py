def replace_letters(word):
    t = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'zeeediiihooooonuuuuutaaaaa')
    return word.translate(t)
