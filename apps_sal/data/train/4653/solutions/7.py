from string import ascii_lowercase as l, ascii_uppercase as u
def next_letter(s): return s.translate(str.maketrans(l + u, l[1:] + l[0] + u[1:] + u[0]))
