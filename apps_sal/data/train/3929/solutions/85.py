def reverse(st):
    words = st.rstrip().split(" ")
    return " ".join(w for w in words[::-1] if w != "")
