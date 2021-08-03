def encode(message, key):
    #    alphabet = {
    #    'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9,
    #    'j' : 10, 'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17,
    #    'r' : 18, 's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25,
    #    'z' : 26
    #    }
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
