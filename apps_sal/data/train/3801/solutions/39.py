def words_to_marks(s):
    abc = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))

    sum = 0

    for char in s:
        sum += abc[char]

    return sum
