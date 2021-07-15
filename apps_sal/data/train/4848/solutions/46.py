def char_freq(message):
    chars = list(message)
    counts = [message.count(char) for char in chars]
    return {chars[i]:counts[i] for i in range(len(chars))}
