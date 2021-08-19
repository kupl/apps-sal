def change(st):
    new = ''
    st = st.lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter in st:
            new += '1'
        else:
            new += '0'
    return new
