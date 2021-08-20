import re


def wanted_words(n, m, forbid_let):
    return [word for word in WORD_LIST if len(word) == n + m and len(re.findall('[aeiou]', word)) == n and (not re.findall('[' + ''.join(forbid_let) + ']', word))]
