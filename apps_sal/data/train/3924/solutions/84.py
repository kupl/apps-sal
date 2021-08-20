def reverse_words(text):
    a = text
    list_1 = []
    list_3 = []
    split = text.split(' ')
    for x in split:
        list_2 = []
        if x == '':
            list_3.append(x)
        else:
            length = len(x)
            for y in range(length - 1, -1, -1):
                list_2.append(x[y])
            final = ''.join(list_2)
            list_3.append(final)
    re_final = ' '.join(list_3)
    return re_final
