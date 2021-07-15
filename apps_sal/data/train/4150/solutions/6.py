import re

def rot13(message):
    pattern1 = re.compile(r'[A-Ma-m]') 
    pattern2 = re.compile(r'[N-Zn-z]')   
    deciphered = []
    for s in message:
        if pattern1.match(s):
            deciphered.append(chr(ord(s) + 13))
        elif pattern2.match(s):
            deciphered.append(chr(ord(s) - 13))
        else:
            deciphered.append(s)
    return ''.join(deciphered)
