def reverse(st):
    st = st.strip()
    s = st.split(' ')
    while '' in s:
        s.remove('')
    while ' ' in s:
        s.remove(' ')
    st = ' '.join(s[::-1])
    return st.rstrip()
