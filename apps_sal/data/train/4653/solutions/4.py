from string import ascii_lowercase as L, ascii_uppercase as U


def next_letter(s):
    return s.translate(str.maketrans(L + U, L[1:] + L[0] + U[1:] + U[0]))
