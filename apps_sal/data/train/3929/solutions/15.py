def reverse(st):
    sv = st.split()
    sv.reverse()
    ss = ""
    for word in sv:
        ss += word
        ss += " "
    ss = ss.strip()
    return ss
