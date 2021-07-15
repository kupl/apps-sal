def abacaba(k):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for i in range(26):
        s = s + alph[i] + s
    return s[k-1]
    
         

