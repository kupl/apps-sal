def remove_duplicate_words(s):
    undupped = []
    for i in s.split():
        if i not in undupped:
            undupped.append(i)
    return ' '.join(undupped)
