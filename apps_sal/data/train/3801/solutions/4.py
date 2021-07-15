def words_to_marks(s):
    base = ord('a') - 1
    return sum(ord(l) - base for l in s)

