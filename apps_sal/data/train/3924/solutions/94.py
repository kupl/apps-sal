def reverse_words(text):
    res = list()
    win = str(text).split()
    for w in win:
        word = str()
        for l in w:
            word = l + word
        res.append(word)
    if '  ' in text:
        return '  '.join(res)
    else:
        return ' '.join(res)
