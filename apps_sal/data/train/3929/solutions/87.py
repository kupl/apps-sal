def reverse(st):
    st = st.split()
    s = ''
    for i in reversed(st):
        s = s + i + ' '
    return s.rstrip()
