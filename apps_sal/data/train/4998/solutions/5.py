from collections import Counter


def wanted_words(n, m, forbid_let):
    result = []
    for word in WORD_LIST:
        if len(word) == n + m:
            letters = Counter(word)
            if sum((letters[c] for c in 'aeiou')) == n and all((c not in word for c in forbid_let)):
                result.append(word)
    return result
