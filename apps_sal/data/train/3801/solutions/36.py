def words_to_marks(s):
    abc = ' abcdefghijklmnopqrstuvwxyz'
    return sum([abc.index(l) for l in s])
