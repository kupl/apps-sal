def words_to_marks(word):
    return sum(ord(char) - 96 for char in word)

