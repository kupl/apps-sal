def remove_duplicate_words(s):
    list1=[]
    [list1.append(x) for x in s.split() if x not in list1]
    return ' '.join(list1)

