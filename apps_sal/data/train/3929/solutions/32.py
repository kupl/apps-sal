def reverse(st):
    # Your Code Here
    a = st.split(' ')
    b = [i for i in a if i != '']
    return ' '.join(b[::-1])
