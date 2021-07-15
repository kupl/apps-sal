def reverse(st):
    result = []
    for w in st.split():
        result.insert(0, w)
    return ' '.join(result)
