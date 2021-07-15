def reverse_words(text):
    ret_text = ''
    text_list = text.split(' ')
    
    for n, i in enumerate(text_list):
        text_list[n] = i[::-1]
    
    for n, i in enumerate(text_list):
        if n != len(text_list) - 1:
            ret_text += f'{i} '
        else:
            ret_text += i
            
    return ret_text
