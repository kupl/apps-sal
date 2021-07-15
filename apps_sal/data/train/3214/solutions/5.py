from string import ascii_lowercase


def change(st):
    source = st.lower()
    return ''.join('1' if q in source else '0' for q in ascii_lowercase)
