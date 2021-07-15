def remove_duplicate_words(s):
    already = []
    for i in s.split():
        if i in already:
            continue
        if i not in already:
            already.append(i)
    return ' '.join(already)

