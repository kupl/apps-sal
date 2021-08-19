def reverse(st):
    word = st.split()
    st2 = []
    for words in word:
        st2.insert(0, words)
    return ' '.join(st2)
