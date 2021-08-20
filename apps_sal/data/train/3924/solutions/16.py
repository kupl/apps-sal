def reverse_words(text):
    rev = text[::-1]
    lst_rev = rev.split(' ')
    lst = lst_rev[::-1]
    str = ' '.join(lst)
    return str
