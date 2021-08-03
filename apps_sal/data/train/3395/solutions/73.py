def remove_duplicate_words(s):
    final = []
    for w in s.split(' '):
        if w not in final:
            final.append(w)
    return ' '.join(final)
