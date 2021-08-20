def encode(message, key):
    coded_message = [ord(char) - 96 for char in message]
    return [digit + int(str(key)[index % len(str(key))]) for (index, digit) in enumerate(coded_message)]
