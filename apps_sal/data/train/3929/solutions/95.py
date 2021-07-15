def reverse(st):
    arr = st.split(" ")[::-1]
    return " ".join([x for x in arr if len(x) > 0])
