def two_sort(array):
    array = sorted(array)
    st = ""
    for c in array[0]:
        st += c + "***"
    return st.rstrip("***")
