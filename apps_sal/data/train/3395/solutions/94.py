def remove_duplicate_words(s):
    S = []
    for word in s.split():
        if word in S:
            continue
        S.append(word)
    return ' '.join(S)

