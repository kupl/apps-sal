from string import ascii_lowercase as l, ascii_uppercase as u
next_letter=lambda s:s.translate(str.maketrans(l+u,l[1:]+l[0]+u[1:]+u[0]))
