def words_to_marks(s):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    total = 0
    for i in range(0, len(s)):
        total = total + 1 + alpha.index(s[i])
    return total
