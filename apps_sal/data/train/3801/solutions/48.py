def words_to_marks(s):
    sum = 0
    d = {alpha: i for i, alpha in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}
    for letter in s:
        sum += d[letter]
    return sum
