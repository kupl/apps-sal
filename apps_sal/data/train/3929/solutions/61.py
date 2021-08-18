def reverse(st):
    spl = st.split()
    string = []
    for i in spl:
        string.insert(0, i)
    return ' '.join(string)
