import re

def word_wrap(text, limit):

    string = text.split()
    res = []
    line = []

    while string: 
        word = string.pop(0)
        if len(''.join(line)) + len(line) + len(word) <= limit: 
            line.append(word)
        else: 
            if len(word) > limit:
                so_far = len(''.join(line)) + len(line) - 1
                available_space = limit - so_far if line else limit
                rest_word = word[available_space - 1:] if line else word[available_space:]
                
                if available_space: 
                    line.append(word[:available_space - 1] if line else word[:available_space])
                    res.append(' '.join(line))
                    string = [rest_word] + string
                else: 
                    res.append(' '.join(line))
                    res.append(word[:limit])
                    string = [word[limit:]] + string
                
                line = []
                
            else: 
                res.append(' '.join(line))
                line = [word]
            
    return '\n'.join(res + [' '.join(line)])
