def to_alternating_case(string):
    result = ''
    lower_vowels = 'abcdefghijklmnopqrstuvwxyz'
    upper_vowels = lower_vowels.upper()
    index = 0
    while index < len(string):
        if string[index] in lower_vowels:
            result += string[index].upper()
        elif string[index] in upper_vowels:
            result += string[index].lower()
        else:
            result += string[index]

        index += 1
    
    return result
