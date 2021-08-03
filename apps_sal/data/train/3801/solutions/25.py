def words_to_marks(s):

    a = "abcdefghijklmnopqrstuvwxyz"
    j = 0
    for i in s:
        j = j + (int(a.index(i)) + 1)

    return j
