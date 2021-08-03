def encode(message, key):
    import string

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # étape 1 : conversion du message en nombres
    code = []
    for i in range(len(message)):
        code += [alphabet.index(message[i]) + 1]
    # étape 2: on ajoute la clef
    keystr = str(key)
    for i in range(len(code)):
        code[i] += int(keystr[i % len(keystr)])

    return code
