def remove_duplicate_words(s):
    uniq = []
    for word in s.split():
        if word not in uniq:
            uniq.append(word)
    return ' '.join(uniq)
