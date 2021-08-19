from collections import deque


def play_pass(s, n):
    d = deque((chr(ord('A') + x) for x in range(26)))
    d.rotate(-n)
    return ''.join((d[ord(c) - ord('A')].lower() if c.isalpha() and i % 2 else d[ord(c) - ord('A')] if c.isalpha() else str(9 - int(c)) if c.isdigit() else c for (i, c) in enumerate(s)))[::-1]
