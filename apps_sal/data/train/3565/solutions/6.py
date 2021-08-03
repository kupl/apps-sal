def solve(st, k):
    for i in range(ord('a'), ord('z') + 1):
        while k and chr(i) in st:
            k -= 1
            st = st.replace(chr(i), '', 1)
    return st
