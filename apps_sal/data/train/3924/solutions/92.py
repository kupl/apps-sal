def reverse_words(text):
    final_string = ''
    for i in [i[::-1] for i in text.split(' ')]:
        final_string += i + ' '
    return final_string[:-1]
