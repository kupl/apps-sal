tbl1 = str.maketrans('aeiou', '12345')
tbl2 = str.maketrans('12345', 'aeiou')


def encode(st):
    return st.translate(tbl1)


def decode(st):
    return st.translate(tbl2)
