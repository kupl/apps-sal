def reverse(st):
    s = st.split(' ')
    return ' '.join([i for i in s[::-1] if i != ''])
