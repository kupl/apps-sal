def words_to_marks(s):
    return sum([ord(char) - 96 for char in s])

