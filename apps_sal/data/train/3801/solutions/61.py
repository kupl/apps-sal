def words_to_marks(s):
    alpha = ' abcdefghijklmnopqrstuvwxyz'
    return sum([alpha.index(c) for c in s])
