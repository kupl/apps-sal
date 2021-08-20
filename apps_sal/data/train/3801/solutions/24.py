import string


def words_to_marks(s):
    result = 0
    alpha = list(string.ascii_lowercase)
    word = ','.join(s).split(',')
    for i in word:
        result += alpha.index(i) + 1
    return result
