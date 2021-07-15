def encryptor(key, message):
    upper_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_alpha = list("abcdefghijklmnopqrstuvwxyz")

    cipher = ""
    for x in message:
        if x in upper_alpha:
            cipher += upper_alpha[(upper_alpha.index(x) + key) % 26] 
        elif x in lower_alpha:
            cipher += lower_alpha[(lower_alpha.index(x) + key) % 26]
        else: 
            cipher += x
    return cipher
