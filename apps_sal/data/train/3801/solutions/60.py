def words_to_marks(s):
    total = 0
    for ltr in s:
        total += (ord(ltr)-96)
    return total

