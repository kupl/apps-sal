def duplicate_encode(word):
    word = word.lower()
    return ''.join(('(' if word.count(x) == 1 else ')' for x in word))
