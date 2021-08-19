def reverse(st):
    st = st.split(' ')
    st = st[::-1]

    st = ' '.join(st)
    st.strip()
    # Your Code Here
    return ' '.join(st.split())
