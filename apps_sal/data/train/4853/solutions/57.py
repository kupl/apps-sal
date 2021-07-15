def double_char(s):
    chars = []
    
    for char in s:
        chars.append(char)
        
    for i in range(len(chars)):
        chars[i] = chars[i] * 2
    
    return ''.join(chars)
