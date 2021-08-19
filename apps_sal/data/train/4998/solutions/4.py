def wanted_words(n, m, forbid_let):
    f = set(forbid_let)
    return [word for word in WORD_LIST if len(word) == n + m and sum((c in 'aeiou' for c in word)) == n and f.isdisjoint(word)]
