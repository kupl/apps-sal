def okkOokOo(s): return ''.join(chr(int(x, 2)) for x in s[:-1].replace(', ', '').upper().replace('O', '0').replace('K', '1').split('? '))
