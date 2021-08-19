def reverse_words(text):
    split_txt = text.split(' ')
    result = ''
    for word in split_txt:
        result += ''.join(word[::-1]) + ' '
    print(result[:-1])
    return result[:-1]
