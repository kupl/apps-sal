def words_to_marks(word):
    abc = ' abcdefghijklmnopqrstuvwxyz'
    return sum([abc.index(el) for el in word])
