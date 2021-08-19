def reverse_words(text):
    new_list = text.split(' ')
    lc = [x[::-1] for x in new_list]
    return ' '.join(lc)
