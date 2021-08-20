def remove_duplicate_words(s):
    lt = []
    for i in s.split():
        if i not in lt:
            lt.append(i)
    return ' '.join(lt)
