def reverse(st):
    # Your Code Here
    list = st.split()
    reverse = list[:: -1]
    return " ".join(reverse)
