def reverse(st):
    words = st.strip().split()
    words = words[::-1]
    return ' '.join(words)
