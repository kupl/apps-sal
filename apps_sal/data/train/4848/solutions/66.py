def char_freq(message):
    char_dict = {}
    
    for letter in message:
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] = char_dict[letter] + 1
                
    return char_dict          
