def words_to_marks(s):
    num = 0
    for character in s:
        num = num + ord(character) - 96
    return num
