def reverse_words(text):
    word_list = text.split()
    reversed_str = ''
    spacer = ''
    if ' ' in text:
        count = 1
        spacer += ' '
        index = text.find(' ')
        while text[index + count] == ' ':
            spacer += ' '
            count += 1
            
    for item in word_list:
        item = item[::-1]
        if len(reversed_str) < 1:
            reversed_str += item
        else:
            reversed_str += (spacer + item)
    return reversed_str
