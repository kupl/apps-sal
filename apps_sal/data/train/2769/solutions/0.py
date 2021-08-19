def decipher(cipher):
    out = ''
    while cipher:
        l = 2 if cipher[0] == '9' else 3
        out += chr(int(cipher[:l]))
        cipher = cipher[l:]
    return out
