def reverse(st):
    list = st.split()
    reverse = list[:: -1]
    return " ".join(reverse)
