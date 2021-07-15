def reverse(st):
    b = st.split()
    return ' '.join([b[i] for i in range(len(b)-1,-1,-1)])

