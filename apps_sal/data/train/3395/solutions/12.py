def remove_duplicate_words(s):
    present = []
    for word in s.split(' '):
        if word not in present:
            present.append(word)
    return ' '.join(present)
