def reverse(st):
    words_list = st.split()
    words_list.reverse()
    st = " ".join(words_list)
    return st
