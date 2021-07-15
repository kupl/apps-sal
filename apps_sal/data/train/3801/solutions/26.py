def words_to_marks(s):
    ergebniss = 0
    for x in s:
        ergebniss += ord(x) - 96
    return ergebniss
