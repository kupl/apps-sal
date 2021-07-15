region = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&" + '"'

def decrypt(encrypted_text):
    if not encrypted_text: return encrypted_text
    
    letters = list(encrypted_text)
    letters[0] = region[-(region.index(letters[0]) + 1)]
    for i in range(1, len(letters)):
        letters[i] = region[region.index(letters[i - 1]) - region.index(letters[i])]
    
    for i in range(1, len(letters), 2):
        letters[i] = letters[i].swapcase()

    return "".join(letters)
    


def encrypt(text):
    if not text: return text
    
    letters = list(text)
    for i in range(1, len(letters), 2):
        letters[i] = text[i].swapcase()
        
    swapped = letters[:]
    for i in range(1, len(letters)):
        letters[i] = region[region.index(swapped[i - 1]) - region.index(swapped[i])]
        
    letters[0] = region[-(region.index(swapped[0]) + 1)]
    return "".join(letters)

