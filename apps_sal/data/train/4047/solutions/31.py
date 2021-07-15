LEET_DICT = {'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3',
             'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!', 'J' : 'J',
             'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0',
             'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : '$', 'T' : '7',
             'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y',
             'Z' : '2'}
def to_leet_speak(english): 
    leet_translation = ''
    for letter in english.upper():
        if letter in LEET_DICT:
            leet_translation += LEET_DICT.get(letter)
        else:
            leet_translation += letter
    return leet_translation     
