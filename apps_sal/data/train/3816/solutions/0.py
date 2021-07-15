from string import ascii_lowercase as al

tbl = str.maketrans(al, al[10:] + al[:10])
def move_ten(st):
    return st.translate(tbl)
