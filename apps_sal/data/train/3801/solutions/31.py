def words_to_marks(s):
    summ = 0
    for x in s:
        for z, y in enumerate('abcdefghijklmnopqrstuvwxyz', 1):
            if y == x:
                summ += z
    return summ
