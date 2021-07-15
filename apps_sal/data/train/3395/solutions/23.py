def remove_duplicate_words(s):
    result = []
    [result.append(w) for w in s.split(' ') if not w in result]
    return ' '.join([x for x in result])
