def reverse_words(text):
    lis = text.split(' ')
    reversed_words = []
    new_sentence = ''
    for word in lis:
        new_word = word[::-1]
        print(new_word)
        reversed_words.append(new_word)
    for word in reversed_words:
        new_sentence += word + ' '
    return new_sentence[0:len(new_sentence) - 1]
