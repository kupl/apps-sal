import string

def xcode(message, key, initShift, is_encode):
    seen, ret, shift = set(), "", initShift
    alphabet = [c for c in key.lower() + string.ascii_lowercase if c.isalpha() and not (c in seen or seen.add(c))]
    for letter in list(message):
        if letter.isalpha():
            new_index = (alphabet.index(letter) + (shift if is_encode else -shift)) % 26
            shift = (alphabet.index(letter) if is_encode else new_index) + 1
            letter = alphabet[new_index]
        ret += letter
    return ret

def encode(message, key, initShift):
    return xcode(message, key, initShift, True)

def decode(message, key, initShift):
    return xcode(message, key, initShift, False)
