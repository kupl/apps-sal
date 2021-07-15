def encode(string):
    string = string.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    st = []
    for l in string:
        if l.isalpha():
            st.append(alph.find(l)+1)
        else:
            st.append(l)
    return ''.join(map(str,st))
