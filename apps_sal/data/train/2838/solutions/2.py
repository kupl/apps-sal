def char_concat(word):
    return ''.join(('{}{}{}'.format(word[n], word[-1 - n], n + 1) for n in range(len(word) // 2)))
