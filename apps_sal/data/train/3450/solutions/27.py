def array(st):
    st = st.replace(" ", "")
    arr = st.split(",")
    if len(arr) <= 2:
        return None
    return " ".join(arr[1:-1])
