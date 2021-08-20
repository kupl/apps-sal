def reverse_words(text):
    t_list = text.split(' ')
    for (i, t_ele) in enumerate(t_list):
        if t_ele == '':
            t_list[i] = t_ele
        else:
            t_list[i] = t_ele[::-1]
    return ' '.join(t_list)
