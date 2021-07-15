key = "GADERYPOLUKI"

def table(key):
    full_key = key.upper() + key.lower()
    even, odd = full_key[::2], full_key[1::2]
    return str.maketrans(even + odd, odd + even)

encode = decode = lambda message: message.translate(table(key))
