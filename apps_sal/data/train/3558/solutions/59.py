def capitalize_word(word):
    init = word[0]
    rem = word[1:len(word)]
    return ''.join([init.upper(), rem])
