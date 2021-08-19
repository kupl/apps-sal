def capitalize_word(word):
    str = ''
    lst = list()
    for i in word:
        lst.append(i)
    lst[0] = lst[0].upper()
    for i in lst:
        str += i
    return str
