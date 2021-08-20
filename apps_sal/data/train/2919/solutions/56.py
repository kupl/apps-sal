def encode(message, key):
    key_tracker = 0
    ciphertext = []
    key = [int(k) for k in str(key)]
    letters = [ord(a) - 96 for a in message]
    for i in range(len(letters)):
        letters[i] += key[key_tracker]
        key_tracker += 1
        if key_tracker == len(key):
            key_tracker = 0
    return letters
