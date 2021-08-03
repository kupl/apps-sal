def remove_duplicate_words(s):
    arr = s.split()
    new = []
    for i in arr:
        if i not in new:
            new.append(i)
    return " ".join(new)
