def decipher(cipher):
    s = ''
    while cipher != '':
        if int(cipher[:3]) <= 122:
            s += chr(int(cipher[:3]))
            cipher = cipher[3:]
        else:
            s += chr(int(cipher[:2]))
            cipher = cipher[2:]
    return s
