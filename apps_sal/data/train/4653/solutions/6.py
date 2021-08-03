from string import ascii_lowercase as low, ascii_uppercase as up


def next_letter(s):
    return s.translate(str.maketrans(
        low + up, low[1:] + low[0] + up[1:] + up[0]))
