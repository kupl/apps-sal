def max_number(n):
    st = [char for char in str(n)]
    st.sort(reverse=True)
    s = int(''.join(st))
    return s
