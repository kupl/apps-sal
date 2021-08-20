def char_freq(message):
    return {chr: message.count(chr) for chr in message}
