import string
alphabet = {key: idx for idx, key in enumerate(string.ascii_lowercase)}


def scramble(s1, s2):
    used_words1 = [0] * 26
    used_words2 = [0] * 26
    for element in s1:
        used_words1[alphabet[element]] += 1
    for element in s2:
        used_words2[alphabet[element]] += 1
    for i in range(26):
        if used_words2[i] > used_words1[i]:
            return False
    return True
