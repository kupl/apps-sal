def char_concat(word, index=1):
    if len(word) < 2:
        return ''
    return word[0:1] + word[-1:] + str(index) + char_concat(word[1:-1], index + 1)
