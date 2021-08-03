def reverse(st):
    return ' '.join([i for i in st.split(' ')[::-1] if len(i) > 0])
