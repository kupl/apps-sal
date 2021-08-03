def words_to_marks(string):
    return sum(ord(char) - 96 for char in string)
