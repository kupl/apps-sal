def reverse_words (string): 
    string = string[::-1] 
    word_r = string.split(' ')
    word_r.reverse()
    output = ' '.join(word_r)
    return output
