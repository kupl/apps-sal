def words_to_marks(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = 0
    for i in s:
        res += alphabet.index(i) + 1
    return res
