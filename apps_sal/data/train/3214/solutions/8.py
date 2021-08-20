def change(st):
    return ''.join(('1' if y in st.lower() else '0' for y in 'abcdefghijklmnopqrstuvwxyz'))
