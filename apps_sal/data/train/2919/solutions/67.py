def encode(message, key):
    msgnumber = [ord(m) - 96 for m in message]
    key = (str(key) * int(len(message) / len(str(key)) + 1))[:len(message)]
    key = [int(k) for k in key]
    return [m + k for (m, k) in zip(msgnumber, key)]
