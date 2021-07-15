def words_to_marks(s):
    return sum(ord(n)-96 for n in s)
