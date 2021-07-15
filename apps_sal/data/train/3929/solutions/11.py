def reverse(st):
    for sentenses in st.split('\n'):
        return(' '.join(sentenses.split()[::-1]))
    return st [::-1]
