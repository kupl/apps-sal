def alternateCase(s):
    cout = []
    
        
    for letter in s:
        if letter == letter.upper():
            cout.append(letter.lower())
        elif letter == letter.lower():
            cout.append(letter.upper())
    return "".join(cout)
