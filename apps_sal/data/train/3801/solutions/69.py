def words_to_marks(s):
    score = 0
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in s:
        index = (alpha.find(char)) + 1
        score += index
    return score
