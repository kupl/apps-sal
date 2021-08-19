def reverse_words(text):
    ls = []
    for i in text.split():
        ls.append(i[::-1])
    if text.find('  ') > -1:
        return '  '.join(ls)
    else:
        return ' '.join(ls)
