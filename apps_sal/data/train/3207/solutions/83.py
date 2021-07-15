def reverseWords(s):
    my_list = s.split(' ')[::-1]
    return ' '.join(my_list)
