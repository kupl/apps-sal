def char_freq(message):
    return {
        m: message.count(m) for m in message
    }
