def array(string):
    list1 = string.split(',')
    if len(list1) <= 2:
        return None
    else:
        return ' '.join(list1[1:-1])

