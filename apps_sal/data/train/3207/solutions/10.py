def reverseWords(str):
    new_arr = []
    for word in str.split():
        new_arr.append(word)
    new_arr.reverse()   
    return ' '.join(new_arr)
