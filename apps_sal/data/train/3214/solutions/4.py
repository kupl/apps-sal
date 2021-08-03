def change(st):
    return ''.join(['1' if i in st.lower() else '0' for i in 'abcdefghijklmnopqrstuvwxyz'])
