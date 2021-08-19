def words_to_marks(s):
    a = [ord(char) - 96 for char in s]
    return sum(a)
