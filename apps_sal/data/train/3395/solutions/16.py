def remove_duplicate_words(s):
    s = s.split()
    unique = []
    for word in s:
        if word not in unique:
            unique.append(word)
    s = ' '.join(unique)
    return s
