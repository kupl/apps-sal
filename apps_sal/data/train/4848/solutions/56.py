def char_freq(message):
    message = sorted(list(message))
    d = {message[i]: message.count(message[i]) for i in range(len(message))}
    return d
