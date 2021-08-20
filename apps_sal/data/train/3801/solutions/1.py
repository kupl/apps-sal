def words_to_marks(s):
    return sum(('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s))
