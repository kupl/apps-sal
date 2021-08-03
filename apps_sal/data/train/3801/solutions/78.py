def words_to_marks(s):
    import string
    alpha = string.ascii_lowercase
    dic = {}
    for char in alpha:
        dic[char] = alpha.index(char) + 1
    score = 0
    for char in s:
        score += dic[char]
    return score
