def filter_words(st):
    st2 = st[0] + st.lower()[1:] 
    return ' '.join((st2.capitalize()).split())

