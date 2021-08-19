from collections import Counter


def char_freq(message: str) -> dict:
    return dict(Counter((c for c in message)))
