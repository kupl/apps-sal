from collections import deque

def encode(message, key):
    out = []
    key = deque(map(int, str(key)))
    for c in message:
        out.append(ord(c) - 96 + key[0])
        key.rotate(-1)
    return out
