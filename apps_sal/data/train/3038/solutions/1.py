def solve(st):
    return min(set(st), key=lambda c: (st.index(c) - st.rindex(c), c))
