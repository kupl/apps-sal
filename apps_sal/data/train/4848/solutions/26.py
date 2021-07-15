def char_freq(message):
    return dict(zip(list(message), [message.count(c) for c in message]))
