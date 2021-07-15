def decipher_message(message):
    side_length = int(len(message) ** .5)
    return "".join(message[i::side_length] for i in range(side_length))
