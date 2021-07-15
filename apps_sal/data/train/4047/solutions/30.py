def to_leet_speak(input_string):
    LEET_DICT = {'A' : '@', 'B' : '8', 'C' : '(', 'D' : 'D', 'E' : '3',
             'F' : 'F', 'G' : '6', 'H' : '#', 'I' : '!', 'J' : 'J',
             'K' : 'K', 'L' : '1', 'M' : 'M', 'N' : 'N', 'O' : '0',
             'P' : 'P', 'Q' : 'Q', 'R' : 'R', 'S' : '$', 'T' : '7',
             'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 'Y' : 'Y',
             'Z' : '2'}
    output_string = ''
    for char in input_string:
        output_string += LEET_DICT.get(char.upper(),char)
    return output_string
