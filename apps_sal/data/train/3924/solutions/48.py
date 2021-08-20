def reverse_words(text):
    txt_lst = text.split(' ')
    res = []
    for item in txt_lst:
        res.append(item[::-1])
    return ' '.join(res)
