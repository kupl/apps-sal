def wanted_words(n, m, f):
    return [i for i in WORD_LIST if len([j for j in i if j in 'aeiou']) == n and len([j for j in i if not j in 'aeiou']) == m and (not any((k in i for k in f)))]
