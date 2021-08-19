def reverseWords(str):
    rev_list = list(str.split(' '))
    rev_str = ''
    for i in range(len(rev_list) - 1, -1, -1):
        rev_str += rev_list[i]
        if i != 0:
            rev_str += ' '
    return rev_str
