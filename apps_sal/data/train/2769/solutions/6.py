def decipher(cipher):
    temp,aus = "",""
    for dig in cipher:
        temp = temp + dig
        if int(temp) >= 97 and int(temp) <= 122:
            aus += chr(int(temp))
            temp = ""
    return aus
