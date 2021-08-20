def remove_duplicate_words(s):
    s = s.split(' ')
    lst = []
    for item in s:
        if item not in lst:
            lst.append(item)
    return ' '.join(lst)
