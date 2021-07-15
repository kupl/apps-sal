def encrypt(text, rule):
    encrypted_text = list(text)
    for i in range(len(encrypted_text)):
        encrypted_text[i] = chr((ord(encrypted_text[i]) + rule) % 256 )
    return "".join(encrypted_text)
