def pseudo_sort(st):
    st = st.replace(",", "")
    st = st.replace("!", "")
    st = st.replace(".", "")
    st = st.replace(":", "")
    st = st.replace(";", "")
    st = st.replace("?", "")
    st = st.split()
    lis1 = [i for i in st if i.islower() == True]
    lis2 = [i for i in st if i[0].isupper() == True]
    lis1.sort(reverse=False)
    lis2.sort(reverse=True)
    return " ".join(lis1 + lis2)
