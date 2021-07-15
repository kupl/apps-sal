def reverse_words(text):
    reverse=''
    for word in text.split(' ')[:-1]:
        reverse+=word[::-1]+' '
    return reverse+text.split(' ')[-1][::-1]
