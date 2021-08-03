def words_to_marks(s):
    i = 0
    for ch in s:
        i = i + ord(ch) - 96
    return i
