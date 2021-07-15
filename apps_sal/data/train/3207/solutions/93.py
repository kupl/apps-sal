def reverseWords(str):
    final_str = ''
    str_lst = str.split(' ')[::-1]
    for word in str_lst:
        final_str += word
        final_str += ' '
    return final_str.strip()
        

