def words_to_marks(s):
    total = 0
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    for eachletter in s:
        total = total + alphabet.index(eachletter)
    return total
