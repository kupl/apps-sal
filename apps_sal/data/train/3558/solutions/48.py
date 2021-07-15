def capitalize_word(word):
    return word[0].upper()+word[1-len(word):] if len(word)!=1 else word[0].upper() 
