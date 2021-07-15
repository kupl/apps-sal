def alternateCase(s):
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = list(upper_letters.lower())
    upper_letters = list(upper_letters)
    
    ans = ''
    index = 0

    while index < len(s):
        char = s[index]
        if char == '' or char == ' ':
            ans += char
            index += 1
            continue
        
        if char in upper_letters:
            ans += char.lower()
        
        if char in lower_letters:
            ans += char.upper()
            
        index += 1

    return ans
