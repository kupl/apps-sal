import string


def words_to_marks(s):
    sum = 0
    for a in s:
        sum = sum + list(string.ascii_lowercase).index(a) + 1
    return sum
