def words_to_marks(s):
    return sum((ord(x) for x in s)) - 96 * len(s)
