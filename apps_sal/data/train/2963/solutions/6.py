def swap(word):
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in word)
