from re import search


def kontti(s):
    words = []
    for word in s.split():
        i = search('[aeiouyAEIOUY]', word)
        if i:
            i = i.start()
            words.append(f'ko{word[i + 1:]}-{word[:i + 1]}ntti')
        else:
            words.append(word)
    return ' '.join(words)
