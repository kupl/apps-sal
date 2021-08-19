def reverse(st):
    a = st.split(' ')
    b = [i for i in a if i != '']
    return ' '.join(b[::-1])
