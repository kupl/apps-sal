def remove_duplicate_words(s):
    a = []
    for i in s.split():
        if i not in a:
            a.append(i)
    return " ".join(a)
