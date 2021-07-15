def hex_to_dec(s):
    
    convert = ''
    dec = 0
    
    for i in range(len(s)):
        
        if s[len(s)-1-i] == '0':
            convert = 0
        if s[len(s)-1-i] == '1':
            convert = 1
        if s[len(s)-1-i] == '2':
            convert = 2
        if s[len(s)-1-i] == '3':
            convert = 3
        if s[len(s)-1-i] == '4':
            convert = 4
        if s[len(s)-1-i] == '5':
            convert = 5
        if s[len(s)-1-i] == '6':
            convert = 6
        if s[len(s)-1-i] == '7':
            convert = 7
        if s[len(s)-1-i] == '8':
            convert = 8
        if s[len(s)-1-i] == '9':
            convert = 9
        if s[len(s)-1-i] == 'a':
            convert = 10
        if s[len(s)-1-i] == 'b':
            convert = 11
        if s[len(s)-1-i] == 'c':
            convert = 12
        if s[len(s)-1-i] == 'd':
            convert = 13
        if s[len(s)-1-i] == 'e':
            convert = 14
        if s[len(s)-1-i] == 'f':
            convert = 15
        
        dec += convert * (16 ** i)
    
    return dec
