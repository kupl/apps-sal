from itertools import cycle 
def encode(message, key):
    # Code here
    return [a + b for a, b in zip(cycle([int(i) for i in str(key)]), [ord(i)-96 for i in message])]
