from string import ascii_uppercase as u, ascii_lowercase as l


def alternateCase(s):
    return s.translate(str.maketrans(u + l, l + u))
