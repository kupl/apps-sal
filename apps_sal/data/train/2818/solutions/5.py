def duplicate_encode(word):
    new_string = ""
    word = word.lower()
    
    for char in word:
        new_string += (")" if (word.count(char) > 1) else "(")
            
    return new_string
