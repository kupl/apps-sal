def words_to_marks(s):
    return sum(ord(x) - 96 for x in s)
