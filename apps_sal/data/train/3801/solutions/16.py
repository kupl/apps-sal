def words_to_marks(s):
    return sum([int(ord(k))-96 for k in s])
