def reverse(st):
    st = st.split(' ')
    st.reverse()
    st = ' '.join(st).rstrip(' ').lstrip(' ')
    st = st.replace('  ', ' ')
    return st.replace('  ', ' ')
