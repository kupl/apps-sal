CIPHER = ("aeiou", "12345")


def encode(st):
    return st.translate(str.maketrans(CIPHER[0], CIPHER[1]))


def decode(st):
    return st.translate(str.maketrans(CIPHER[1], CIPHER[0]))
