def word_pattern(pattern, string):
    match = {}
    
    if len(pattern) != len(string.split()): return False
    
    for c, word in zip(pattern, string.split()):
        # For a new character in pattern
        if c not in match: 
            # If word has already been assigned to a character, return false
            if word in list(match.values()): return False
            
            # else assign the word to the character
            match[c] = word
        
        # Match the word with the one assigned to the character
        if match[c] != word: return False
    
    return True

