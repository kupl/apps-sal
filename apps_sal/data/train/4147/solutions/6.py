from string import ascii_uppercase as letters, digits


def play_pass(s, n):
    return "".join(c.lower() if i & 1 else c
                   for i, c in enumerate(s.upper().translate(
                       str.maketrans(letters + digits, letters[n:] + letters[:n] + digits[::-1])
                   )))[::-1]
