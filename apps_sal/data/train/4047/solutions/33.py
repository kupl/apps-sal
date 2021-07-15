def to_leet_speak(input_str):
    LEET_DICT = {'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3',
             'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!', 'J' : 'J',
             'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0',
             'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : '$', 'T' : '7',
             'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y',
             'Z' : '2'}
    
    output_str = ''
    for char in input_str.upper():
        if char in LEET_DICT.keys():
            output_str += LEET_DICT[char]
        else:
            output_str += char
    return output_str
