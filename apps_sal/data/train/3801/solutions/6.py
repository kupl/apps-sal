def words_to_marks(s):
    return sum((ord(e) - 96 for e in s))
