def reverse_words(st):
    return " ".join("".join(reversed(wr)) for wr in st.split(' '))
