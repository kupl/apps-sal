def encode(text, key):
    
    string = "abcdefghijklmnopqrstuvwxyz"
    string_me = key+string
    periods = []
    spaces = []
    commas = []
       
    string_me = list(dict.fromkeys(string_me))

    
    for x in range(0, len(text)):
        if text[x] == ".":
            periods.append(x)
        elif text[x] == ",":
            commas.append(x)
        elif text[x] == " ":
            spaces.append(x)
            
    text = text.replace(".", " ").replace(",", " ").split()  
    
    word = 0
    
    new_word = []
    
    while word < len(text):
        
        for x in range(0, len(text[word])):
            
            if text[word][x].isupper():
                
                if string_me.index(text[word][x].lower())+x+1 >= 26:
                    
                    number = string_me.index(text[word][x].lower())+x+1
                    
                    while number >= 26:
                        number -= 26
                    
                    new_word.append(string_me[number].upper())
                else:
                    new_word.append(string_me[string_me.index(text[word][x].lower())+x+1].upper())
                
            else:
                
                if string_me.index(text[word][x])+x+1 >= 26:
                    
                    number = string_me.index(text[word][x].lower())+x+1
                    
                    while number >= 26:
                        number -= 26
                        
                    new_word.append(string_me[number])
                else:
                    new_word.append(string_me[string_me.index(text[word][x].lower())+x+1])
            
        text[word] = "".join(new_word)
        new_word = []
        word += 1
        
                       
    text = list("".join(text))
    
    newwww = periods+spaces+commas
    
    newwww.sort()

    if newwww:
        for x in newwww:
            text.insert(x, " ")
        
    for x in periods:
        text[x] = "."
    for x in commas:
        text[x] = ","
    
    return("".join(text))

    
def decode(text, key):
    
    string = "abcdefghijklmnopqrstuvwxyz"
    string_me = key+string
    periods = []
    spaces = []
    commas = []
       
    string_me = list(dict.fromkeys(string_me))
    
    for x in range(0, len(text)):
        if text[x] == ".":
            periods.append(x)
        elif text[x] == ",":
            commas.append(x)
        elif text[x] == " ":
            spaces.append(x)
            
    text = text.replace(".", " ").replace(",", " ").split()  
    
    word = 0
    
    new_word = []
    
    while word < len(text):
        
        for x in range(0, len(text[word])):
            
            if text[word][x].isupper():
                

                
                if string_me.index(text[word][x].lower())-x-1 >= 26:
                    
                    number = string_me.index(text[word][x].lower())-x-1
                    
                    while number >= 26:
                        number -= 26
                    
                    new_word.append(string_me[number].upper())
                
                elif string_me.index(text[word][x].lower())-x-1 < 0:
                    
                    number = string_me.index(text[word][x].lower())-x-1
                    
                    while number < 0:
                        number += 26
                        
                    new_word.append(string_me[number].upper())
                else:
                    new_word.append(string_me[string_me.index(text[word][x].lower())-x-1].upper())
                
            else:


                
                if string_me.index(text[word][x])-x-1 >= 26:
                    
                    number = string_me.index(text[word][x].lower())-x-1
                    
                    while number >= 26:
                        number -= 26
                    new_word.append(string_me[number])    
                elif string_me.index(text[word][x].lower())-x-1 < 0:
                    
                    number = string_me.index(text[word][x].lower())-x-1
                    
                    while number < 0:
                        number += 26
                        
                    new_word.append(string_me[number])
                else:
                    new_word.append(string_me[string_me.index(text[word][x].lower())-x-1])
            
        text[word] = "".join(new_word)
        new_word = []
        word += 1
        
                       
    text = list("".join(text))
    
    newwww = periods+spaces+commas
    
    newwww.sort()

    if newwww:
        for x in newwww:
            text.insert(x, " ")
        
    for x in periods:
        text[x] = "."
    for x in commas:
        text[x] = ","
    
    return("".join(text))

