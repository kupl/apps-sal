def stringy(size):
    st = "1"
    i = 0
    while i < size - 1:
        if st[i] == "1":
            st = st + "0"
        else:
            st = st + "1"
        i += 1
    return st
