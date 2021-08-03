def char_freq(message):
    s = set(message)
    n = [message.count(i) for i in s]
    return dict(zip(s, n))
