def caeser(message, key):
    return ''.join(('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(el) + key) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')] if el in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else el for el in message.upper()))
