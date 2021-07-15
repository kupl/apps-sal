def reverse(st):
    return ' '.join([s for s in st.rstrip(' ').split(' ')[::-1] if s != ''])
