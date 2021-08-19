def reverse_words(text):
    output = ''
    word = ''
    for i in text:
        if i != ' ':
            word += i
        else:
            output += word[::-1]
            output += i
            word = ''
    output += word[::-1]
    return output
