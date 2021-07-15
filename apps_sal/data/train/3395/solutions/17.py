def remove_duplicate_words(s):
    final = []
    for s in s.split():
        if s not in final:
            final.append(s)
    return ' '.join(final)
