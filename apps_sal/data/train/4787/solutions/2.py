def remove(s: str) -> str:
    r = s.replace('!', '')
    return r + '!' * (len(s) - len(r))
