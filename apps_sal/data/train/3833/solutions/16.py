import string

def longest(s1, s2):
    
    comb = []
    alphabet = {}
    ind = 0
    
    for letter in s1:
        if letter in comb:
            pass
        else:
            comb.append(letter)
    
    for letters in s2:
        if letters in comb:
            pass
        else:
            comb.append(letters)
    
    lowerCase = list(string.ascii_lowercase)
    
    for letters in lowerCase:
        ind+=1
        alphabet[letters] = ind
    
    for x in range(len(comb)):
        for i in range(len(comb)-1):
            if alphabet[comb[i]] > alphabet[comb[i+1]]:
                comb[i], comb[i+1] = comb[i+1], comb[i]

    comb = ''.join(comb)
    
    return comb
