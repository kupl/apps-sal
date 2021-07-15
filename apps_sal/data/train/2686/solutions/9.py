from string import ascii_letters

tr=str.maketrans(ascii_letters,'bcdEfghIjklmnOpqrstUvwxyzA'*2)

def changer(s):
    return s.translate(tr)
