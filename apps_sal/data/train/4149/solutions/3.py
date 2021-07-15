from string import digits as d, ascii_lowercase as l, ascii_uppercase as u

tbl = str.maketrans(
    d             + l               + u,
    d[5:] + d[:5] + l[13:] + l[:13] + u[13:] + u[:13],
)

def ROT135(input):
    return input.translate(tbl)
