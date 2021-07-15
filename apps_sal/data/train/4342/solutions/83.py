def no_space(word):
    new_word = ''
    
    for char in word:
        if char is not ' ':
            new_word = new_word + char
            
    return new_word


