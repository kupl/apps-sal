def words_to_marks(s):
    return sum(ord(c) for c in s) - 96*len(s)
