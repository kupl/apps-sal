def capitalize_word(word):
    newword = ""
    x=0
    for n in word:
        if x ==0:
            newword+=(word[0].upper())
            x+=1
        else:
            newword+=n
    
            
        
    
    return newword
