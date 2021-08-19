def wanted_words(n, m, forbid_let):
    result = []
    for word in WORD_LIST:
        if set(forbid_let) & set(word):
            continue
        vowels = sum((1 for c in word if c in 'aeiou'))
        if vowels == n and len(word) == m + n:
            result.append(word)
    return result
