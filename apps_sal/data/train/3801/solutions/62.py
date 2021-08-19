def words_to_marks(s):
    import string
    letters = string.ascii_lowercase
    score = 0
    for letter in s:
        score += letters.index(letter) + 1
    return score
