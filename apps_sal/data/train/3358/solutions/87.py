def correct(string):
    x = "501"
    y = "SOI"
    other = string.maketrans(x, y)
    return(string.translate(other))
