def first_non_consecutive(list):
    tmp = ''
    for item in list:
        if tmp == '':
            tmp = str(item)
        else:
            if item == int(tmp) + 1:
                tmp = str(item)
            else:
                return item
