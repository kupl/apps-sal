def reverse(st):
    st = st.split(' ')
    st = st[::-1]
    st = ' '.join(st)
    st.strip()
    return ' '.join(st.split())
