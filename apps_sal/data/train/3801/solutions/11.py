def words_to_marks(letters):
    result = 0
    for letter in letters:
        result += ord(letter) - 96
    return result
