trans = str.maketrans('ao', 'ou')


def convert(st):
    return st.translate(trans)
