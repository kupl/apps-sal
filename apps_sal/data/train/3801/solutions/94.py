def words_to_marks(s):
    sum = 0
    for letters in s:
        sum += ord(letters) - 96
    return sum
