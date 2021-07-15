def capitalize(s,ind):
    str_lst = [letter for letter in s]
    for index in ind:
        try:
            str_lst[index] = str_lst[index].upper()
        except:
            pass
    return ''.join(str_lst)
