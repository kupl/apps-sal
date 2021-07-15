def play_pass(s, n):
    passphrase = list(s)
    for i in range(0, len(s)):
        if passphrase[i].isalpha():
            ascii = ord(passphrase[i].lower())
            passphrase[i] = chr(ascii+n-26) if ascii+n > 122 else chr(ascii+n)
            passphrase[i] = passphrase[i].lower() if i % 2 == 1 else passphrase[i].upper()
        if passphrase[i].isdigit():
            passphrase[i] = str(9 - int(passphrase[i]))
            
    return ''.join(passphrase[::-1])
