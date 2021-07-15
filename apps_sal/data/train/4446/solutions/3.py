def words_to_sentence(words):
    st = ""
    for x in range(len(words)):
        st = st + words[x] + ' '
    return st.strip()


