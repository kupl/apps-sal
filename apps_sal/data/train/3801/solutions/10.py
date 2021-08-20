def words_to_marks(word):
    return sum((ord(ch) - 96 for ch in word))
