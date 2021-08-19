def words_to_marks(word):
    s = ' abcdefghijklmnopqrstuvwxyz'
    a = 0
    for el in word:
        a += s.index(el)
    return a
