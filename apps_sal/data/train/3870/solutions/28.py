def solve(s):
    new_s = [x if x.isalpha() else '' for x in s[::-1]]
    
    for char in new_s:
        if char == '':
            new_s.remove(char)
    
    for i in range(len(s)):
        if s[i] == ' ':
            new_s.insert(i, s[i])
    
    return ''.join(new_s)

