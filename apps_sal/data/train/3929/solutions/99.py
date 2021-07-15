def reverse(st):
    st=st.split(" ")
    for i in st:
        if i=="":
            st.remove(i)
    st=st[::-1]
    st=" ".join(st)
    return st.strip()
