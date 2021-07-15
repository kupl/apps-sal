def array(string):
    
    s = string.split(',')
    s2 = ' '.join(s[1:len(s)-1])
    return s2 if s2 is not '' else None
