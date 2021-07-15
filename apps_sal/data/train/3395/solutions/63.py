def remove_duplicate_words(s):
    result = []
    s = s.split(' ')
    for i, word in enumerate(s):
        if word not in result:
            result.append(word)
        else:
            pass
    return ' '.join(result)
