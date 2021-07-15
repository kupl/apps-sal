def two_sort(array):
    
    array.sort()
    
    word = array[0]
    
    new_word = ""
    
    for letter in word:
        new_word+=letter
        new_word+="***";
        
    return new_word[:-3]

