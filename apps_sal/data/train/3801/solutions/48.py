def words_to_marks(s):
    # using enumerate() ;)
    sum = 0
    d = {alpha: i for i, alpha in enumerate('abcdefghijklmnopqrstuvwxyz', start=1)}  # key-val pairs of all alphabets
    for letter in s:
        sum += d[letter]
    return sum
