def grille(message, code):
    binary = str(bin(code)[2:].zfill(len(message)))
    print(str(bin(code)[2:]))
    i = 0
    decoded = ""
    if(len(binary) > len(message)):
        while (i < len(message)):
            if (binary[i + (len(binary) - len(message))] == '1'):
                decoded += message[i]
            i += 1
    while (i < len(message)):
        if (binary[i] == '1'):
            decoded += message[i]
        i += 1
    return decoded
