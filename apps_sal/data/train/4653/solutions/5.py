from string import ascii_letters as a, ascii_lowercase as al, ascii_uppercase as au


def next_letter(string):
    return string.translate(str.maketrans(a, al[1:] + al[0] + au[1:] + au[0]))
