def reverseWords(str):

    str_list=str.split(' ')
    rev_list=str_list[::-1]
    rev_str=' '.join(rev_list)
    return rev_str
