def encode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(v, str(i))
    return st


def decode(st):
    for i, v in enumerate("aeiou", start=1):
        st = st.replace(str(i), v)
    return st
