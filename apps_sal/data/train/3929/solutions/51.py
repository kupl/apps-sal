def reverse(st):
    # Your Code Here
    s = st.rstrip()
    s = s.split()
    return " ".join(s[::-1])
