def reverse(st):
    words = st.split()
    words = list(reversed(words))
    st = ' '.join(words)
    return st
